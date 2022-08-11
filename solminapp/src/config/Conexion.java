
package config;

import java.sql.Connection;
import java.sql.DriverManager;

public class Conexion {
    Connection con;
    public Conexion(){
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            con=DriverManager.getConnection("jdbc:mysql://192.168.1.179:3306/solmin","rootdos","root");
        } catch (Exception e) {
            System.err.println("Error:"+e);
        }        
    }
    public Connection getConnection(){
        return con;
    }
  }
