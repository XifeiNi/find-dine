import { StyleSheet } from "react-native";
import Metrics from "src/config/metrics";
import AppStyles from "src/config/styles";
import { isIphoneX } from "src/lib/isIphoneX";

const styles = StyleSheet.create({
  container: {
    alignItems: "center",
    borderColor: AppStyles.colors.grey,
    borderWidth: StyleSheet.hairlineWidth,
    flexDirection: "row",
    height: isIphoneX() ? 74 : 50,
    justifyContent: "space-between",
    paddingBottom: isIphoneX() ? 24 : 0,
    paddingHorizontal: 8,
  },
  customContainer: {
    alignItems: "center",
    borderColor: AppStyles.colors.grey,
    borderWidth: StyleSheet.hairlineWidth,
    flexDirection: "row",
    height: 50,
    justifyContent: "space-between",
    paddingBottom: 0,
    paddingHorizontal: 8,
  },
  btn: {
    alignItems: "center",
    borderRadius: 16,
    height: 32,
    justifyContent: "center",
    overflow: "hidden",
    width: 32,
  },
  input: {
    borderColor: AppStyles.colors.grey,
    borderRadius: 24,
    borderWidth: StyleSheet.hairlineWidth,
    height: 36,
    marginVertical: 8,
    width: Metrics.screenWidth / 2 - 16,
  },
});
export default styles;
