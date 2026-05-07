
import {Fragment,memo,useCallback,useContext,useEffect} from "react"
import {ReflexEvent,applyEventActions,isTrue} from "$/utils/state"
import {IconButton as RadixThemesIconButton} from "@radix-ui/themes"
import {ColorModeContext,EventLoopContext} from "$/utils/context"
import {jsx} from "@emotion/react"






export const Iconbutton_iconbutton_661c74222fefe790e1eff2612de2002c = memo(({children}) => {
    const [addEvents, connectErrors] = useContext(EventLoopContext);
const { toggleColorMode } = useContext(ColorModeContext)
const on_click_dedd885ce47a15c1666b026c014cf563 = useCallback(((_e) => (toggleColorMode(_e))), [addEvents, ReflexEvent, toggleColorMode])



    return(
        jsx(RadixThemesIconButton,{css:({ ["padding"] : "6px", ["position"] : "fixed", ["top"] : "2rem", ["right"] : "2rem", ["background"] : "transparent", ["color"] : "inherit", ["zIndex"] : "20", ["&:hover"] : ({ ["cursor"] : "pointer" }) }),onClick:on_click_dedd885ce47a15c1666b026c014cf563},children)
    )
});
