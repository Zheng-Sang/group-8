<template>
  <div>
    <!-- <b-jumbotron header="Recommend for you">
      <b-button variant="outline-dark" @click="get_recommend()">refresh</b-button>
    </b-jumbotron> -->

    <!-- <b-container fluid="sm">
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
          <img v-for="image in images" :key="image.url" v-bind:src="image.url" v-bind:alt="image.alt" />
          <b-img :src="items[recomm - 1].src" height='400' rounded></b-img>
        </template>
        <b-carousel-slide-caption>
          <h4>{{items[recomm - 1].title}}</h4>
        </b-carousel-slide-caption>
        <b-button :href="items[recomm - 1].link" variant="dark" @click="handle_buy(items[recomm - 1].id)">Learn more</b-button>
      </b-carousel-slide>
      </b-carousel>
    </b-container> -->

<!-- navbar section -->
<div>
  <b-navbar toggleable="lg" type="dark" class="navbar navbar-custom">

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="nav-item active">
        <b-nav-item href="#" class="nav-link">&lsaquo;</b-nav-item>
      </b-navbar-nav>
      <div class="navbar-header">  
        <b-navbar-brand class="navbar-brand">Customize Your Trip</b-navbar-brand>
      </div>
      <b-navbar-nav class="nav-item active ml-auto">
        <b-nav-item href="#" class="nav-link">&rsaquo;</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>

<!-- customer info section -->
<div>
  <b-jumbotron border-variant="dark" class="jumbotron jumbotron-custom">
    <p class="jumbotron-header">name holder</p>

  <li class="jumbotron-body">
    <p>phone: +1 000-000-000</p>
    <p>MileagePlus: XXXXXXXX</p>
    <p>account balance: {{account}}</p>
  </li>
  </b-jumbotron>
</div>

<!-- recommendation section -->
  <div>
    <b-container fluid="lg">
      <ul>
        <li v-for="recomm in recomms" :key="recomm.title">       
          <b-card no-body class="overflow-hidden card">
            <b-card-img :src="items[recomm - 1].src" class="rounded-0"></b-card-img>
            <b-card-body class="card-body">
              <b-card-text class="card-title">
                {{items[recomm - 1].title}}
              </b-card-text>
              <b-card-text class="card-text">
                <p>price: {{items[recomm - 1].price}} miles</p>
              </b-card-text>
              <a :href="items[recomm].link" variant="dark" class="card-link">more information</a>
              <b-button @click="handle_buy(items[recomm])" :disabled="account < items[recomm].price" class="card-button" >buy with miles</b-button>
            </b-card-body>
            <br>
          </b-card>
        </li>
      </ul>
      <!-- <b-button variant="outline-dark" @click="get_recommend()">test recommendation button</b-button> -->
    </b-container>
  </div>

  <!-- view all products -->
  <a href=#>view all products</a>

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
                src: 'https://media.united.com/images/Media%20Database/SDL/MileagePlus/premier/upgrade/_3WS0289-drink2x.png',
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html',
                price: 3000},
        
        {id: 2, title: 'Increase Baggage Allowance', 
                src: 'https://mightyfares.mightytravels.com/mightytravels-images/uploads/2019/08/best-checked-luggage-bags-e1545310304513.jpg',
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html',
                price: 3000},
        
        {id: 3, title: 'Wi-Fi',  
                src: 'https://www.unitedwifi.com/assets/images/wifi-hero.jpg',
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html',
                price: 3000},
        
        {id: 4, title: 'Priority Boarding', 
                src: "https://liveandletsfly.boardingarea.com/wp-content/uploads/2018/03/United-Airlines-Priority-Boarding.jpg",
                link: 'https://www.united.com/ual/en/us/fly/mileageplus/awards/upgrade.html',
                price: 3000},
      ],
      recomms: [1,2,3],
      account: 5000,
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
      this.account = this.account - product.price;
      const buy_url = 'http://localhost:5000/db/buy'
      axios.put(buy_url, {
        data: {
          customer_id: '1',
          product_id: product.id
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

.navbar-custom {
  background-color: #030438;
}

.navbar-custom .nav-item.active .nav-link,
.navbar-custom .nav-item:hover .nav-link {
    color: #ffffff;
    font-size: 120%;
}

.navbar-custom .navbar-header {
    text-align: center;
    width: 100%;
}
.navbar-custom .navbar-brand {float:none;}

.jumbotron-custom {
  background: #ffffff;
  padding-top: 36px;
  padding-bottom: 36px;
}

.jumbotron-custom .jumbotron-header {
    text-align: left;
    padding-left: 8px;
    width: 100%;
    font-weight: 400;
    font-size: 150%;
}

.jumbotron-custom .jumbotron-body {
    text-align: left;
    width: 100%;
    font-weight: 100;
    font-size: 100%;
}

.card {
  max-width: 250px;
}

.card .card-body .card-title {
  font-size: 100%;
  font-weight: 500;
  text-align: left;
}

.card .card-body .card-text {
  font-size: 80%;
  text-align: left;
  padding-top: 0px;
}

.card .card-body .card-link {
  font-size: 80%;
  text-align: left;
}

.card .card-body .card-button {
  color: #ffffff;
  background-color: #216de7d2;
  border-color: #ffffff;
}
</style>