import { StyleSheet } from 'react-native';
import AppStyles from 'src/config/styles';

const styles = StyleSheet.create({
    listTopView: {
        alignItems: 'center',
        flexDirection: 'row',
        justifyContent: 'space-between',
        padding: 8,
        paddingHorizontal: 12
    },
    active: {
        color: AppStyles.colors.grey,
        fontSize: 14,
        fontWeight: 'bold',
    },
    watchAll: {
        color: AppStyles.colors.accentColor,
        fontSize: 14,
        fontWeight: 'bold',
    },
    headView: {
        alignItems: 'center',
        marginHorizontal: 4
    },
    headSub: {
        alignItems: 'center',
        backgroundColor: AppStyles.colors.grey,
        borderRadius: 24,
        height: 48,
        justifyContent: 'center',
        margin: 4,
        width: 48,
    },
    nameText: {
        fontSize: 12
    },
    headText: {
        fontSize: 12,
        textAlign: 'center',
        width: 64,
    },
    absoluteView: {
        backgroundColor: AppStyles.colors.white,
        borderColor: AppStyles.colors.white,
        borderRadius: 16,
        borderWidth: 1,
        bottom: -4,
        position: 'absolute',
        right: -2,
    },
    itemView: {
        alignItems: 'center',
        justifyContent: 'center',
        margin: 4,
    },
    nameView: {
        alignItems: 'center',
        flexDirection: 'row',
        marginTop: 10,
        paddingHorizontal: 4
    },
    onlineDot: {
        backgroundColor: AppStyles.colors.onlineGreen,
        borderRadius: 5,
        height: 10,
        marginRight: 4,
        width: 10,
    }
});

export default styles;
