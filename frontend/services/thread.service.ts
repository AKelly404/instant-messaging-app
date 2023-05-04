import { Thread } from '../models/thread'

export class ThreadService {
    async getAll():Promise<Thread[]> {
        const allThreads = await fetch("http://127.0.0.1:8000/threads/")
        // debugger
        return await allThreads.json();
    }
}