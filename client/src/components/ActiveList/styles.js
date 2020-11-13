import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  item: {
    alignItems: "center",
    flexDirection: "row",
    justifyContent: "space-between",
    paddingLeft: 16,
    paddingRight: 12,
    paddingVertical: 8,
  },
  userName: {
    flex: 1,
    fontSize: 15,
    paddingLeft: 8,
    textAlign: "left",
  },
  wave: {
    height: 28,
    resizeMode: "contain",
    width: 28,
  },
});

export default styles;
