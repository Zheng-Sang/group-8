const mongoose = require('mongoose')
const express = require('express')
const app = express()
const port = 3000
const bodyParser = require('body-parser')
//const config = require('./config/index')
const seederService = require('./services/seeder.service');

app.use(bodyParser.json())


url = "mongodb://127.0.0.1:27017/UA1";
db = mongoose.connect(url,function(err){
    if(!err)
    {
        console.log("Connect to DB Successfully!");
    }else{
        console.log("Error to connect to DB");
    }
})

var userSchema = mongoose.Schema({
    customer_id : String,
    product_list : [String]
})

var userModel = mongoose.model('User', userSchema);

app.put('/application/json', function(req, res){
    collection = db.collection('Users');
    data = req.body;
    collection.insert(data, function(err, result) { 
        if(err)
        {
            console.log('Error:'+ err);
            return;
        } 
    })
})
 



const corsConfig = function(req, res, next) {
    res.header('Access-Control-Allow-Origin', 'http://localhost:8080')
    res.header('Access-Control-Allow-Credentials', true)
    res.header('Access-Control-Allow-Methods', 'GET,HEAD,OPTIONS,POST,PUT')
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization')
    next()
}

app.use(corsConfig);

const apiRoutes = require('./routes/api');
app.use('/api', apiRoutes);

if (config.seedData) {
    seederService.seedData()
}

app.listen(port, () => console.log(`Example app listening on port ${port}!`))