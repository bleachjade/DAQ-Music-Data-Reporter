var MongoClient = require('mongodb').MongoClient;
var url = "mongodb+srv://feen:feen@cluster0.mo20d.mongodb.net/Song?retryWrites=true&w=majority";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("MusicDataReporter");
  dbo.collection("Artists").find({}, { projection: { _id: 0, artist: 1, number_of_fans: 1 } }).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});

