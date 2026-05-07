import {Box as RadixThemesBox,Heading as RadixThemesHeading} from "@radix-ui/themes"
import {Fragment,useEffect} from "react"
import {jsx} from "@emotion/react"





export default function Component() {





  return (
    jsx(Fragment,{},jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "auto|auto", ["padding"] : "20px" })},jsx(RadixThemesHeading,{align:"center",color:"amber",css:({ ["width"] : "auto|auto", ["fontFamily"] : "Comic Relief", ["--default-font-family"] : "Comic Relief" }),size:"9"},"Notes"))),jsx("title",{},"Appnotes | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}