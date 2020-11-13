import { StyleSheet, Dimensions } from "react-native";
import AppStyles from "src/config/styles";

const DIMENSION_WIDTH = Dimensions.get("window").width;
const GRAY = "#757E90";

const styles = StyleSheet.create({
  container: {
    backgroundColor: AppStyles.colors.lightWhite,
    flex: 1,
  },
  containerMessage: {
    alignItems: "center",
    flex: 1,
    flexDirection: "row",
    justifyContent: "flex-start",
    paddingHorizontal: 10,
    width: DIMENSION_WIDTH - 100,
  },
  avatar: {
    borderRadius: 30,
    height: 60,
    marginRight: 20,
    marginVertical: 15,
    width: 60,
  },
  message: {
    color: GRAY,
    fontSize: 12,
    paddingTop: 5,
  },
});

export default styles;
