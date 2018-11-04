import React from "react";
import { View, Text } from "react-native";
import LinearGradient from "react-native-linear-gradient";
export default class TopBrand extends React.Component {
  render() {
    return (
      <LinearGradient
        style={styles.wrapperview}
        colors={["#0080FB", "#5eb0ff", "white"]}
        start={{ x: 0, y: 0 }}
        end={{ x: 0, y: 1 }}
      >
        <Text style={styles.logoText}>{this.props.content}</Text>
      </LinearGradient>
    );
  }
}

const styles = {
  wrapperview: {
    height: 200,
    width: "100%",
    justifyContent: "center",
    alignItems: "center",
  },
  logoText: {
    color: "white",
    fontSize: 40,
  }
};
