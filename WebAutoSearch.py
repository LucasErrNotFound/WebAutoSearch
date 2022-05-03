#All imported packages
import importlib
import os
import AUTOCHROME
import AUTOMSEDGE
import AUTOFIREFOX

def options(): #This is where all options are available displayed in the main menu

    user_input = input('-----> ').upper()[0] #Uppercase or lowercase input by the user is valid

    if user_input == 'A': #If the user enters "A" or "a", then the chromedriver will execute
        os.system('cls')  #The chromedriver is an executable
        print('''
    _   _   _ _____ ___   ____ _   _ ____   ___  __  __ _____
   / \ | | | |_   _/ _ \ / ___| | | |  _ \ / _ \|  \/  | ____|
  / _ \| | | | | || | | | |   | |_| | |_) | | | | |\/| |  _|
 / ___ \ |_| | | || |_| | |___|  _  |  _ <| |_| | |  | | |___
/_/   \_\___/  |_| \___/ \____|_| |_|_| \_\\___/|_|  |_|_____|''')

        print("\nCONTROLS:\nPress 'alt' to auto search\nPress 'esc' to exit")
        print("<<AUTOCHROME ACTIVATED>>")
        AUTOCHROME.process1() #This executes the "process1" function in AUTOCHROME.py
        os._exit(0)

    elif user_input == 'B': #If the user enters "B" or "b", then the msedgedriver will execute
        os.system('cls')    #The msedgedriver is an executable
        print('''
    _   _   _ _____ ___  __  __ ____  _____ ____   ____ _____
   / \ | | | |_   _/ _ \|  \/  / ___|| ____|  _ \ / ___| ____|
  / _ \| | | | | || | | | |\/| \___ \|  _| | | | | |  _|  _|
 / ___ \ |_| | | || |_| | |  | |___) | |___| |_| | |_| | |___
/_/   \_\___/  |_| \___/|_|  |_|____/|_____|____/ \____|_____|''')

        print("\nCONTROLS:\nPress 'alt' to auto search\nPress 'esc' to exit")
        print("<<AUTOMSEDGE ACTIVATED>>")
        AUTOMSEDGE.process2() #This executes the "process2" function in AUTOEDGE.py
        os._exit(0)

    elif user_input == 'C': #If the user enters "B" or "b", then the geckodriver will execute
        os.system('cls')    #The geckdriver is an executable
        print('''
    _   _   _ _____ ___  _____ ___ ____  _____ _____ _____  __
   / \ | | | |_   _/ _ \|  ___|_ _|  _ \| ____|  ___/ _ \ \/ /
  / _ \| | | | | || | | | |_   | || |_) |  _| | |_ | | | \  /
 / ___ \ |_| | | || |_| |  _|  | ||  _ <| |___|  _|| |_| /  \ 
/_/   \_\___/  |_| \___/|_|   |___|_| \_\_____|_|   \___/_/\_\ ''')

        print("\nCONTROLS:\nPress 'alt' to auto search\nPress 'esc' to exit")
        print("<<AUTOFIREFOX ACTIVATED>>")
        AUTOFIREFOX.process3() #This executes the "process3" function in AUTOFIREFOX.py
        os._exit(0)

    elif user_input == 'D':
        contributors()

    elif user_input == 'E':
        help()

    elif user_input == 'F':
        license()

    elif user_input == "G":
        about()

    elif user_input == 'H':
        print("Terminating...")
        os._exit(0)

    elif user_input not in ("A","B","C","D","E","F","G"): #If user enters letters that are not in options, then it will clear the command line and loop back to main
        os.system('cls')
        main()

def help(): #For users who wants additional info

    os.system('cls')
    print('''
 _   _ _____ _     ____
| | | | ____| |   |  _ \ 
| |_| |  _| | |   | |_) |
|  _  | |___| |___|  __/
|_| |_|_____|_____|_|

 ___ _   _ _____ ___  ____  __  __    _  _____ ___ ___  _   _
|_ _| \ | |  ___/ _ \|  _ \|  \/  |  / \|_   _|_ _/ _ \| \ | |
 | ||  \| | |_ | | | | |_) | |\/| | / _ \ | |  | | | | |  \| |
 | || |\  |  _|| |_| |  _ <| |  | |/ ___ \| |  | | |_| | |\  |
|___|_| \_|_|   \___/|_| \_\_|  |_/_/   \_\_| |___\___/|_| \_|''')

    print("\nThe following information can provide additional guidance for the users of this script.")
    print("Please use this script for educational purposes only and not for malicious purposes.")
    print("\nCONTROLS\t\t\t\t\t\t\t\tFUNCTION")
    print("\n- PRESS <esc>\t\t\t\t\t\t\t\tUse to exit the browser but it will not kill the entire script")
    print("- PRESS <alt>\t\t\t\t\t\t\t\tUse to auto search the data inside your clipboard")
    print("\nNOTE:")
    print("\nPlease do not rush the use of this script like there's no tomorrow, please take your time,")
    print("and wait for the scripts and browsers to load in first before you even start pressing <alt>.")
    print("\nSound good and ready to go? Press Y to continue")
    crap = input('-----> ').upper()[0]

    while True: #It will loop until the correct letter is entered

        if crap == "Y":
            main()
            break

        elif crap not in ("Y"):
            print("Wrong Letter")
            help()
            break

def license(): #This opens the license

    os.system('cls')
    print('''
 _     ___ ____ _____ _   _ ____  _____
| |   |_ _/ ___| ____| \ | / ___|| ____|
| |    | | |   |  _| |  \| \___ \|  _|
| |___ | | |___| |___| |\  |___) | |___
|_____|___\____|_____|_| \_|____/|_____|''')

    print('''\n\t\t\t\tApache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS
   
   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.
      
   Copyright 2022 Kódikas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
''')

    print("\nSound good? Press Y to continue:")
    foo = input('-----> ').upper()[0]

    while True: #It will loop until the correct letter is entered

        if foo == "Y":
            main()
            break

        elif foo not in ("Y"):
            license()
            break

def about():

    os.system('cls')
    print('''
    _    ____   ___  _   _ _____
   / \  | __ ) / _ \| | | |_   _|
  / _ \ |  _ \| | | | | | | | |
 / ___ \| |_) | |_| | |_| | | |
/_/   \_\____/ \___/ \___/  |_|''')

    print('''\nWhat is this script all about?
    
    WebAutoSearch is a tool for everyone who finds it difficult to search for something, 
    as well as for the busy guys. This program can automatically search the information in your 
    clipboard and send it to the web browser of your choice. If utilized appropriately,
    this tool may be really useful for your duties.''')
    print("\nGot it? Press Y to continue:")
    bar = input('-----> ').upper()[0]

    while True: #It will loop until the correct letter is entered

        if bar == "Y":
            main()
            break

        elif bar not in ("Y"):
            about()
            break

def contributors():

    os.system('cls')
    print('''
[+]======================================================================[+]
 |   ____ ___  _   _ _____ ____  ___ ____  _   _ _____ ___  ____  ____    |
 |  / ___/ _ \| \ | |_   _|  _ \|_ _| __ )| | | |_   _/ _ \|  _ \/ ___|   |
 | | |  | | | |  \| | | | | |_) || ||  _ \| | | | | || | | | |_) \___ \   |
 | | |__| |_| | |\  | | | |  _ < | || |_) | |_| | | || |_| |  _ < ___) |  |
 |  \____\___/|_| \_| |_| |_| \_\___|____/ \___/  |_| \___/|_| \_\____/   |
[+]======================================================================[+]

This section is all about giving credit to those who contributed to work in this
open source python project. To those who contributed here, I just wanted to say 
thank you so much for your patience, kindness, and hard work. I'm sure that this
project will grow with all your implementations and ideas, without it, this won't
exist, and your name will not be written. I know this project is not yet matured,
because there's still so many missing points and features that I haven't added.

    "Continue to work, and your work will become a treasure" - 6H0$T

To those who contributed in this project, feel free to add your name with this
kind of format:

            [NO.] << NAME << WHAT DID YOU D0
            
  CONTRIBUTORS: 

    [1] << Kódikas << The one who created the idea
    [2] <<  6H0$T  << The one who coded 90% of the script
    [3] << 
                                                                        
                       
                                                                   
                                                                        ''')
    print("\nYou feel good now? Enter Y to continue:")
    snatch = input('-----> ').upper()[0]

    while True: #It will loop until the correct letter is entered

        if snatch == "Y":
            main()
            break

        elif snatch not in ("Y"):
            contributors()
            break

def main():

    os.system('cls')
    print('''
 [+]    
  | __        __   _       _         _       ____                      _
  | \ \      / /__| |__   / \  _   _| |_ ___/ ___|  ___  __ _ _ __ ___| |__
  |  \ \ /\ / / _ \ '_ \ / _ \| | | | __/ _ \___ \ / _ \/ _` | '__/ __| '_ \ 
  |   \ V  V /  __/ |_) / ___ \ |_| | || (_) |__) |  __/ (_| | | | (__| | | |
  |    \_/\_/ \___|_.__/_/   \_\__,_|\__\___/____/ \___|\__,_|_|  \___|_| |_| v0.1.0
  |
  |[+]Company   :  Kódikas
  |[+]Coded     :  6H0$T
  |[+]Youtube   :  https://www.youtube.com/channel/UC6PXnf0CRjymeNcrLVxMrsg
  |[+]Github    :  https://github.com/K0dikas
 [+]==============================================================================[+]''')

    print("\n ACTIVATED! PLEASE CHOOSE YOUR DESIRED OPTIONS:\n")
    print(" [A] << AUTOCHROME\t<< www.google.com\n [B] << AUTOMSEDGE\t<< www.bing.com\n [C] << AUTOFIREFOX\t<< www.duckduckgo.com\n [D] << CONTRIBUTORS\n [E] << HELP\n [F] << LICENSE\n [G] << ABOUT\n [H] << EXIT")
    options()

if __name__ == '__main__':
    main()