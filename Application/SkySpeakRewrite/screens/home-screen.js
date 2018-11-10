import React from "react";
import { View, TextInput, TouchableOpacity, Text } from "react-native";
import TopBrand from "../components/login-screen/topbranding";
import LinearGradient from "react-native-linear-gradient";
import moment from "moment";
import Icon from "react-native-vector-icons/Ionicons";
import Snackbar from "react-native-snackbar";

export default class Home extends React.Component {
  static navigationOptions = {
    header: null
  };

  constructor() {
    super();
    this.state = {
      message: ""
    };
  }

  sendMessage = () => {
    sender = this.props.navigation.getParam("name");
    message = this.state.message;
    date = moment().format("YYYY-MM-DD");
    dragonURL = "http://" + global.dragonIP + "/upload";
    // serverURL = "http://18.216.42.131/api/postmessage";

    fetch(dragonURL, {
      method: "POST",
      body: JSON.stringify({
        sender: sender,
        content: message,
        date: date
      })
    }).then(response => {
      Snackbar.show({ title: "Sent!" });
      this.setState({ message: "" });
    });
  };

  render() {
    var message = this.props.navigation.getParam("name");
    return (
      <LinearGradient
        style={styles.container}
        colors={["#0080FB", "#5eb0ff", "#0080FB"]}
        start={{ x: 0, y: 0 }}
        end={{ x: 0, y: 1 }}
      >
        <TopBrand content={message} />
        <View style={styles.row}>
          <TextInput
            placeholder="Write something"
            onChangeText={text => {
              this.setState({ message: text });
            }}
            style={styles.inputfield}
            value={this.state.message}
            placeholderTextColor="white"
          />
          <TouchableOpacity onPress={this.sendMessage} style={{ width: "30%" }}>
            <LinearGradient
              style={styles.connectbutton}
              colors={["white", "white"]}
            >
              <Icon name="md-send" />
              <Text style={styles.connecttext}>Send Message</Text>
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </LinearGradient>
    );
  }
}

const styles = {
  container: {
    backgroundColor: "white",
    height: "100%",
    width: "100%"
  },
  inputfield: {
    marginLeft: 10,
    width: "70%"
  },
  row: {
    flexDirection: "row",
    width: "100%"
  },
  connectbutton: {
    marginLeft: 10,
    height: 50,
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 100,
    width: 100
  },
  connecttext: {
    color: "grey"
  }
};
