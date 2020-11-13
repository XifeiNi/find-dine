import { StyleSheet } from "react-native";
import Metrics from "src/config/metrics";
import AppStyles from "src/config/styles";

const styles = StyleSheet.create({
  container: {
    backgroundColor: AppStyles.colors.black,
    flex: 1,
    flexDirection: "column",
  },
  preview: {
    alignItems: "center",
    flex: 1,
    justifyContent: "flex-end",
  },
  capture: {
    alignSelf: "center",
    backgroundColor: AppStyles.colors.grey,
    borderRadius: 75,
    flex: 0,
    margin: 20,
    padding: 15,
    paddingHorizontal: 20,
  },
  absoluteView: {
    alignItems: "center",
    bottom: 0,
    justifyContent: "space-between",
    left: 0,
    position: "absolute",
    top: 50,
    width: Metrics.screenWidth,
  },
  head: {
    height: 50,
    padding: 16,
    width: Metrics.screenWidth,
  },
});

export default styles;
