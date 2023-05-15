import { Message } from "../../../models/message"

interface MessageListProps {
    message: Message
}

function MessageList(properties: MessageListProps) {
    return (
    <div className='message' key={properties.message.id}>
        <div>{properties.message.id}</div>
        <div>{properties.message.text}</div>
    </div>
    )
}

export default MessageList