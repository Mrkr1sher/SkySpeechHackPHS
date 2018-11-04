package com.iskyspeak.skyspeak;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Printer;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;

import android.util.Log;
import android.widget.Button;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.InetAddress;
import java.net.UnknownHostException;

import java.io.BufferedWriter;

public class MainActivity extends AppCompatActivity {

    private Socket socket;

    private static final int serverPort = 1234;
    private static String serverIp = "172.16.243.226";

    private PrintWriter out;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        new Thread(new ClientThread()).start();




        Button fab = (Button) findViewById(R.id.fab);

        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Log.d("Network", "Clicked");


                String payload = "Test text four";


                try {
                    if(out == null) {
                        out = new PrintWriter(new BufferedWriter(
                                new OutputStreamWriter(socket.getOutputStream())),
                                true);
                    }
                }catch(IOException e){
                    Log.d("Netwrok","asdas");
                }

                new SendMessageTask().execute();

            }
        });
    }

    private class SendMessageTask extends AsyncTask<String, Void, Void>{

        protected Void doInBackground(String ... params){

            try{
                Log.d("Network","Reached Four");
                out.println("test output");

            } catch (Exception e){
                Log.d("Network connection", "exception");
            }

            return null;

        }


    }

    class ClientThread implements Runnable{


        @Override
        public void run(){

            try{

                InetAddress serverAdd = InetAddress.getByName(serverIp);

                socket = new Socket(serverAdd, serverPort);

            }catch (UnknownHostException e){

                System.out.print("Uncown host");

            }catch(IOException e){

            }

        }

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
