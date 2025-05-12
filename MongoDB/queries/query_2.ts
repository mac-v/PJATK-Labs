// Task description:
// Return a single woman of Chinese nationality

import { Collection } from "mongodb";
import connectToDatabase from "../db-connection.ts";
import saveToFile from "../utils.ts";

interface Person {
  sex: string;
  nationality: string;
}
async function execQuery() {
  const db = await connectToDatabase();
  const peopleCollection: Collection<Person> = db.collection<Person>("people");
  const res = await peopleCollection.findOne({
    sex: "Female",
    nationality: "China",
  });

  saveToFile("data/results_2.json", res);
}

execQuery();
