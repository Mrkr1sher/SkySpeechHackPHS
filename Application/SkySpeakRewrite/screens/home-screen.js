import React from "react";
import { View, TextInput, TouchableOpacity, Text } from "react-native";
import TopBrand from "../components/login-screen/topbranding";
import LinearGradient from "react-native-linear-gradient";

export default class Home extends React.Component {
  static navigationOptions = {
    header: null
  };

  render() {
    var message = "Welcome, " + this.props.navigation.getParam("name");
    return (
      <View style={styles.container}>
        <TopBrand content={message} />
        <View style={styles.row}>
          <TextInput
            placeholder="Write something"
            onChangeText={text => {
              this.setState({ name: text });
            }}
            style={styles.inputfield}
          />
          <TouchableOpacity onPress={() => {}} style={{width: "30%"}}>
            <LinearGradient
              style={styles.connectbutton}
              colors={["white", "white"]}
            >
              <Text style={styles.connecttext}>Send Message</Text>
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </View>
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
