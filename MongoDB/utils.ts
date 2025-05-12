import { promises as fs } from "fs"; 

async function saveToFile(filePath: string, res: object | null): Promise<void> {
  try {
    const content = res ? JSON.stringify(res, null, 2) : "No results";
    await fs.writeFile(filePath, content);
    console.log(`Data saved to ${filePath}`);
  } catch (error) {
    console.error(`Failed to save data to ${filePath}:`, error);
  }
}

export default saveToFile;