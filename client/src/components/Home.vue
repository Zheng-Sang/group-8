<template>
    <div>
    <b-jumbotron header="Recommend for you">
      <b-button variant="outline-dark" @click="get_recommend()">refresh</b-button>
    </b-jumbotron>

    <b-container fluid="sm">
      <b-carousel id="carousel1"
                  style="text-shadow: 1px 1px 2px #333;"
                  controls
                  indicators
                  background="#f0f0f0"
                  :interval="4000"
                  img-width="600"
                  img-height="300"
                  v-model="slide"
                  @sliding-start="onSlideStart"
                  @sliding-end="onSlideEnd"
      >

      <b-carousel-slide v-for="recomm in recomms" :key="recomm.id">
        <template v-slot:img>
          <!-- <img v-for="image in images" :key="image.url" v-bind:src="image.url" v-bind:alt="image.alt" /> -->
          <b-img :src="items[recomm - 1].src" height='400' rounded></b-img>
        </template>
        <b-carousel-slide-caption>
          <h4>{{items[recomm - 1].title}}</h4>
        </b-carousel-slide-caption>
        <b-button :href="items[recomm - 1].link" variant="dark" @click="handle_buy(items[recomm - 1].id)">Learn more</b-button>
      </b-carousel-slide>

      </b-carousel>
    </b-container>

    <br>
    <b-jumbotron header="All Products"></b-jumbotron>

    <b-container fluid="lg">
      <ul>
        <li v-for="item in items" :key="item.title">       
          <b-card no-body class="overflow-hidden" style="max-width: 540px;">
            <b-row no-gutters>
              <b-col md="6">
                <b-card-img :src="items[item.id - 1].src" class="rounded-0"></b-card-img>
              </b-col>
              <b-col md="6">
                <b-card-body>
                  <b-card-body-title>
                    {{item.title}}
                  </b-card-body-title>
                  <b-card-text>
                    <p>{{item.description}}</p>
                  </b-card-text>
                  <b-button :href="item.link" variant="dark" @click="handle_buy(items[recomm - 1].id)">get with miles</b-button>
                </b-card-body>
              </b-col>
            </b-row>
            <br>
          </b-card>
        </li>
      </ul>
    </b-container>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      items: [
        {id: 1, title: 'Seat Upgrade', 
                description: 'item1-description',
                src: 'https://media.united.com/images/Media%20Database/SDL/MileagePlus/premier/upgrade/_3WS0289-drink2x.png',
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html'},
        
        {id: 2, title: 'Increase Baggage Allowance', 
                description: 'item2-description', 
                src: 'https://mightyfares.mightytravels.com/mightytravels-images/uploads/2019/08/best-checked-luggage-bags-e1545310304513.jpg',
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html'},
        
        {id: 3, title: 'Wi-Fi', 
                description: 'item3-description', 
                src: 'https://www.unitedwifi.com/assets/images/wifi-hero.jpg',
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html'},
        
        {id: 4, title: 'Private Screening', 
                description: 'item4-description', 
                src: "https://media.united.com/images/Media%20Database/SDL/Travel/onboard-experience/inflight-entertainment_header_three_1136x3201x.png",
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html'},
        
        {id: 5, title: 'Priority Boarding', 
                description: 'item5-description', 
                src: "https://liveandletsfly.boardingarea.com/wp-content/uploads/2018/03/United-Airlines-Priority-Boarding.jpg",
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html'},
        
        {id: 6, title: 'Share Miles', 
                description: 'item6-description', 
                src: "https://www.creditcards.com/credit-card-news/wp-content/uploads/pooling-miles-lg.png",
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html'},
        
        {id: 7, title: 'In-flight Meals', 
                description: 'item7-description', 
                src: "https://media.united.com/images/Media%20Database/SDL/United/pod-premeal/preorder1-16/Preorder-meals_desktop.jpg",
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html'},
        
        {id: 8, title: 'Gift Cards', 
                description: 'item8-description', 
                src: "https://i.kinja-img.com/gawker-media/image/upload/c_scale,f_auto,fl_progressive,q_80,w_1600/qq8rdj0xsydjtbfkysyh.jpg",
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html'},
        
        {id: 9, title: 'Shopping', 
                description: 'item9-description', 
                src: "https://www.nerdwallet.com/assets/blog/wp-content/uploads/2018/07/20180725-travel-shopping-portal-bonus-631x250.jpg",
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html'},
      ],
      recomms: [1,2,3],
      slide: 0,
      sliding: null,
    }
  },
  methods: {
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    },
    get_recommend() {
      const getRecommend_url = 'http://localhost:5000/'
      axios.get(getRecommend_url, {
                    params: {
                        customer_id: '1'
                    }
                })
                .then((response) => {
                  console.log(this.recomms);
                  var arr = response.data;
                  this.recomms = arr.map(Number);
                  console.log(this.recomms);
                })
                .catch(function (error) {
                  console.log(error);
                });
    },
    handle_buy(product) {
      console.log('Clicked', product);
      const buy_url = 'http://localhost:5000/db/buy'
      axios.put(buy_url, {
        data: {
          customer_id: '1',
          product_id: product
        }
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
