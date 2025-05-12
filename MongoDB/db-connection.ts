import { MongoClient, Db } from "mongodb";
import { config as configDotenv } from "dotenv";

configDotenv();

const username: string | undefined = process.env.MONGO_USERNAME;
const password: string | undefined = process.env.MONGO_PASSWORD;
const clusterUrl: string | undefined = process.env.MONGO_CLUSTER_URL;
const dbName: string | undefined = process.env.MONGO_DB_NAME;

if (!username || !password || !clusterUrl || !dbName) {
  throw new Error("Missing required environment variables for MongoDB connection.");
}

const uri: string = `mongodb+srv://${username}:${password}@${clusterUrl}/${dbName}?retryWrites=true&w=majority`;

let client: MongoClient | null = null;

async function connectToDatabase(): Promise<Db> {
  if (!client) {
    client = new MongoClient(uri);
    await client.connect();
    console.log("Connected to MongoDB!");
  }
  return client.db(dbName);
}

export default connectToDatabase;