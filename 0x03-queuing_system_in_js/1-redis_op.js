import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error('Redis client not connected to the server:', error.message);
});

function setNewSchool(schoolName, value){
	client.set(schoolName value, (error, reply)=>{
	if(error){
	console.error(error)}
	else {
	redis.print}
	});
};
 function displaySchoolValue(schoolName){
	 redis.get(schoolName, (error, reply)=>{
	 if(error){
        console.error(error)}
        else {
	cosole.log(reply)}
        });
})
 }
