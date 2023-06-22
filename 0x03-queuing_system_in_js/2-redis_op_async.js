import redis from 'redis';
import { promisify } from 'util';

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

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName){
	try {
	  let result =getAsync(schoolName)
	  cosole.log(result)
	} catch (error) {
	  console.error(error);
	}
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
