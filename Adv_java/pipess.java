import java.io.*;
import java.nio.ByteBuffer;
import java.nio.channels.Pipe;
class pipess{
    public static void main(String[] args) throws IOException {
        Pipe pipe = Pipe.open();
        Pipe.SinkChannel sinkChannel = pipe.sink();
        @SuppressWarnings("unused")
        String str = "CSE406 Advance Java";
        ByteBuffer bb = ByteBuffer.allocate(1024);
        bb.clear();
        bb.flip();
        while(bb.hasRemaining()){
            sinkChannel.write(bb);
        }
        Pipe.SourceChannel sourceChannel = pipe.source();
        bb = ByteBuffer.allocate(512);
        while (sourceChannel.read(bb)>0) {
            bb.flip();
            while (bb.hasRemaining()) {
                char sc = (char)bb.get();
                System.out.println(sc);
            }
            bb.clear();
        }
    }
}