<template>
  <div id="app">
    <main>
      <div class = "ua_ui">
        <img class = "ui" src = "@/assets/ua.png" />
      </div>

<!--        <div class = "basic_info">May 21 ALB - BEJ</div>-->
<!--        <div class = "sub_info">Oneway, 1 traveler</div>-->


<!--      <div class = "price">-->
<!--        <p style="text-align:left;">-->
<!--          Total:-->
<!--          <span style="float:right;">-->
<!--              $200.00-->
<!--          </span>-->
<!--        </p>-->
<!--      </div>-->

<!--      <div class = "baggage">-->
<!--        <input type = "button" class = baggage_font value = "View checked bag charges" />-->
<!--      </div>-->

      <div class = "from">From*</div>
      <div class = "from_box">
        <input type = "text" class = "from_bar" placeholder = "From City or Airport" />

      </div>

      <div class = "to">To*</div>
      <div class = "to_box">
        <input type = "text" class = "to_bar" placeholder = "To City or Airport" />
      </div>

      <div class = "date">Date*</div>
      <div class = "date_box">
        <input type = "text" class = "date_bar" placeholder = "Date" />
      </div>

      <div class = button>
        <input class = continue_font type = "button" onclick = "location.href = 'https://www.united.com/en/us/united-mileageplus-signin';" value = "Continue" />
        &nbsp; &nbsp; &nbsp;
        <input class = reset_font type = "button" onclick = "location.href = 'https://www.united.com/en/us/united-mileageplus-signin';" value = "Reset" />
      </div>


    </main>

  </div>


</template>

<script>
export default {
  name: 'App',

}
</script>

<style>
  *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body{
    font-family: 'montserrat', sans-serif;
  }
  #app{
    background-image: url('./assets/blue.png');
    background-size: cover;
    background-position: bottom;
    transition: 0.4s;
  }
  main{
    min-height: 100vh;
    padding: 25px;
    background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.001), rgba(0, 0, 0, 0.15));
    /*text-align: center;*/
  }

  /*.very_top{*/
  /*  text-align: center;*/
  /*  display: inline-block;*/
  /*  padding: 10px 40px;*/
  /*  background-color: #353075;*/
  /*}*/
  /*.very_top .basic_info{*/
  /*  color: #ffffff;*/
  /*  font-size: 40px;*/
  /*  font-weight: 500;*/

  /*}*/

  /*.very_top .sub_info{*/
  /*  color: #ffffff;*/
  /*  font-size: 25px;*/
  /*  font-weight: 300;*/
  /*}*/

  .ua_ui .ui{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 300px;
    height: auto;
    padding: 5px;
  }

  .from{
    color: dimgrey;
    font-size: 25px;
    text-shadow: 1px 1px rgba(0, 0, 0, 0.25);
  }



  .from_box{
    width: 100%;
    margin-bottom: 30px;
  }
  .from_box .from_bar{
    display: block;
    width: 100%;
    padding: 15px;

    color: #313131;
    font-size: 20px;

    appearance: none;
    border:none;
    outline: none;
    background: none;

    box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.25);
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 0px 16px 0px 16px;
    transition: 0.4s;
  }

  .to_box{
    width: 100%;
    margin-bottom: 30px;
  }
  .to_box .to_bar{
    display: block;
    width: 100%;
    padding: 15px;

    color: #313131;
    font-size: 20px;

    appearance: none;
    border:none;
    outline: none;
    background: none;

    box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.25);
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 0px 16px 0px 16px;
    transition: 0.4s;
  }

  .date{
    color: dimgrey;
    font-size: 25px;
    text-shadow: 1px 1px rgba(0, 0, 0, 0.25);
  }
  .date_box{
    width: 100%;
    margin-bottom: 30px;
  }
  .date_box .date_bar{
    display: block;
    width: 100%;
    padding: 15px;

    color: #313131;
    font-size: 20px;

    appearance: none;
    border:none;
    outline: none;
    background: none;

    box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.25);
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 0px 16px 0px 16px;
    transition: 0.4s;
  }
  .to{
    color: dimgrey;
    font-size: 25px;
    text-shadow: 1px 1px rgba(0, 0, 0, 0.25);
  }


  /*.price{*/
  /*  display: inline-block;*/
  /*  padding: 10px 155px;*/
  /*  background-color: aliceblue;*/
  /*}*/
  /*.price .total{*/
  /*  float: left;*/
  /*}*/

  /*.price .amount{*/
  /*  float: right;*/
  /*}*/

  .button{
    display: inline-block;

  }
  .button .continue_font{
    background-color:#849fe3;
    border-radius:28px;
    border:1px solid #4e6096;
    display:inline-block;
    cursor:pointer;
    color:#ffffff;
    font-family:Arial;
    font-size:17px;
    padding:16px 52px;
    text-decoration:none;
  }
  .button .continue_font :hover {
    background:linear-gradient(to bottom, #008CBA 5%, #008CBA 100%);
    background-color:#008CBA;
  }
  .continue_button .continue_font :active {
    position:relative;
    top:1px;
  }

  .button .reset_font{
    background-color:#849fe3;
    border-radius:28px;
    border:1px solid #4e6096;
    display:inline-block;
    cursor:pointer;
    color:#ffffff;
    font-family:Arial;
    font-size:17px;
    padding:16px 52px;
    text-decoration:none;
  }
  .button .reset_font :hover {
    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);
    background-color:#6c7c7c;
  }
  .button .reset_font :active {
    position:relative;
    top:1px;
  }

</style>
