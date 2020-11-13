import { StyleSheet } from 'react-native';
import AppStyles from 'src/config/styles';

const styles = StyleSheet.create({
    item: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        paddingHorizontal: 16,
        paddingVertical: 8,
    },
    nameView: {
        flex: 1,
        justifyContent: 'center',
        paddingHorizontal: 8,
    },
    head: {
        color: AppStyles.colors.black,
        fontSize: 16,
        textAlign: 'left'
    },
    sub: {
        color: AppStyles.colors.grey,
        paddingTop: 4
    },
    icon: {
        alignItems: 'center',
        justifyContent: 'center',
        paddingHorizontal: 12,
    },
    hView: {
        backgroundColor: AppStyles.colors.lightWhite
    },
    header: {
        color: AppStyles.colors.grey,
        fontSize: 14,
        fontWeight: 'bold',
        paddingHorizontal: 16,
        paddingVertical: 12,
    },
    groupView: {
        alignItems: 'center',
        flexDirection: 'row',
        paddingVertical: 12
    },
    grpIcn: {
        paddingHorizontal: 16
    },
    grpText: {
        fontSize: 15
    }
});

export default styles;
