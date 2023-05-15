import { Thread } from '../models/thread'
import { Message } from '../models/message'

export class ThreadService {
    async getAll():Promise<Thread[]> {
        const allThreads = await fetch("http://127.0.0.1:8000/threads/")
        // debugger
        return await allThreads.json();
    }

    async getMessages(threadID: string):Promise<Message[]> {
        const allMessages = await fetch(`http://127.0.0.1:8000/threads/${threadID}/messages`)
        return await allMessages.json();
    }
}
