
import {Fragment,memo,useContext,useEffect} from "react"
import {isTrue} from "$/utils/state"
import {ColorModeContext} from "$/utils/context"
import {jsx} from "@emotion/react"






export const Cond_comp_d9a8c10ddfd105c865d3be08c3f7c7c0 = memo(({children}) => {
    const { resolvedColorMode } = useContext(ColorModeContext)



    return(
        ((resolvedColorMode?.valueOf?.() === "light"?.valueOf?.())?(children?.at?.(0)):(children?.at?.(1)))
    )
});
