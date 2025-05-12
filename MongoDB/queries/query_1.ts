// Task description:
// Return a single person from the database

import { Collection } from "mongodb";
import connectToDatabase from "../db-connection.ts";
import saveToFile from "../utils.ts";

interface Person {}
async function execQuery() {
  const db = await connectToDatabase();
  const peopleCollection: Collection<Person> = db.collection<Person>("people");
  const res = await peopleCollection.findOne();

  saveToFile("data/results_1.json", res);
}

execQuery();
