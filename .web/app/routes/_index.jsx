import {Box as RadixThemesBox,Heading as RadixThemesHeading} from "@radix-ui/themes"
import {Fragment,useEffect} from "react"
import {jsx} from "@emotion/react"





export default function Component() {





  return (
    jsx(Fragment,{},jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "20px" })},jsx(RadixThemesHeading,{align:"left",color:"amber",css:({ ["width"] : "auto|auto", ["fontFamily"] : "Comic Relief", ["--default-font-family"] : "Comic Relief", ["sticky"] : "left", ["margin"] : "20px" }),size:"9"},"Notes"),jsx(RadixThemesBox,{},jsx(RadixThemesBox,{className:"cardNotes"},"NOTAS"),jsx(RadixThemesBox,{className:"cardNotes"},"NOTAS")))),jsx("title",{},"Appnotes | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}