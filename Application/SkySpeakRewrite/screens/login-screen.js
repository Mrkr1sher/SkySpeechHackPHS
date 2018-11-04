import React from "react";
import { View, TextInput, TouchableOpacity, Text } from "react-native";
import TopBrand from "../components/login-screen/topbranding";
import LinearGradient from "react-native-linear-gradient";

export default class Login extends React.Component {
  static navigationOptions = {
    header: null
  };
  constructor() {
    super();
    this.state = {
      name: ""
    };
  }

  render() {
    return (
      <View style={styles.container}>
        <TopBrand content="SkySpeech" />
        <TextInput
          placeholder="What's your name?"
          onChangeText={text => {
            this.setState({ name: text });
          }}
          style={styles.inputfield}
        />
        <TouchableOpacity
          onPress={() => {
            this.props.navigation.navigate("Home", { name: this.state.name });
          }}
        >
          <LinearGradient
            style={styles.connectbutton}
            colors={["white", "white"]}
          >
            <Text style={styles.connecttext}>Get Started</Text>
          </LinearGradient>
        </TouchableOpacity>
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
    marginLeft: 10
  },
  connectbutton: {
    width: "30%",
    marginLeft: 10,
    height: 50,
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 100
  },
  connecttext: {
    color: "grey"
  }
};
