#!/usr/bin/env pythonw
#!/usr/bin/env ffmpeg

#################################

#NPR Loudness Tool
#The NPR(R) Loudness Tool (NLT) checks the levels of an audio file or files and indicates if they meet Public Radio Satellite System(R) (PRSS(R)) submission standards (http://prss.org/loudness). The NLT provides the option to adjust levels such that the resulting file is within the PRSS specifications.  Specifically, it adjusts the Integrated Loudness and the True Peaks, then saves the adjusted file.  You can install the NLT on your Mac or PC to check the levels of your audio files.
#The NLT is available at http://prss.org/loudness/tool.  
#License
#NPR Loudness Tool (to check and adjust the loudness levels of audio files)

#Copyright © 2016 NPR 

#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.  In addition, the names of NPR, NPR Labs, and the PRSS may not be used for publicity purposes to endorse or promote products based on this program without express prior written permission.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program.  If not, see http://www.gnu.org/licenses/gpl-3.0.en.html. 
#FFmpeg library

#Copyright © 2012 Clément Bœsch

#The NPR Loudness Tool uses the f_ebur128.c library, which is code of FFmpeg, https://www.ffmpeg.org/, licensed under the GPL 3 or later, http://www.gnu.org/licenses/gpl-3.0.en.html, and its source can be downloaded here:  https://ffmpeg.org/doxygen/2.8/f__ebur128_8c_source.html.   NPR does not own this code.  

# 

#Loudness Standards
#The PRSS Audio Loudness Standard has been set at -24 Loudness Units Relative to Full Scale (LUFS), ± 2 Loudness Units (LU), audio peaks ≤ -3 dBFS for sample peaks or ≤ -2 dBTP for True Peaks, meaning producers should strive to set their programs’ audio levels at -24 LUFS, with a deviation range of ± 2 LU and an audio peak at or below -3 dBFS or -2 dBTP.  See http://prss.org/loudness.  
#NPR Labs
#NPR Labs is the nation’s only not-for-profit broadcast technology research and development center.
#Help
#You may contact NPR about this program at prsshelp@npr.org, or at 800.971.7677.  
#GNU GENERAL PUBLIC LICENSE

#Version 3, 29 June 2007

#Copyright © 2007 Free Software Foundation, Inc. <http://fsf.org/>

#Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

#Preamble

#The GNU General Public License is a free, copyleft license for software and other kinds of works.

#The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.

#When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things.

#To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.

#For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.

#Developers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal permission to copy, distribute and/or modify it.

#For the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software. For both users' and authors' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions.

#Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users' freedom to change the software. The systematic pattern of such abuse occurs in the area of products for individuals to use, which is precisely where it is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users.

#Finally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free.

#The precise terms and conditions for copying, distribution and modification follow.

#TERMS AND CONDITIONS

#0. Definitions.

#“This License” refers to version 3 of the GNU General Public License.

#“Copyright” also means copyright-like laws that apply to other kinds of works, such as semiconductor masks.

#“The Program” refers to any copyrightable work licensed under this License. Each licensee is addressed as “you”. “Licensees” and “recipients” may be individuals or organizations.

#To “modify” a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy. The resulting work is called a “modified version” of the earlier work or a work “based on” the earlier work.

#A “covered work” means either the unmodified Program or a work based on the Program.

#To “propagate” a work means to do anything with it that, without permission, would make you directly or secondarily liable for infringement under applicable copyright law, except executing it on a computer or modifying a private copy. Propagation includes copying, distribution (with or without modification), making available to the public, and in some countries other activities as well.

#To “convey” a work means any kind of propagation that enables other parties to make or receive copies. Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying.

#An interactive user interface displays “Appropriate Legal Notices” to the extent that it includes a convenient and prominently visible feature that (1) displays an appropriate copyright notice, and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided), that licensees may convey the work under this License, and how to view a copy of this License. If the interface presents a list of user commands or options, such as a menu, a prominent item in the list meets this criterion.

#1. Source Code.

#The “source code” for a work means the preferred form of the work for making modifications to it. “Object code” means any non-source form of a work.

#A “Standard Interface” means an interface that either is an official standard defined by a recognized standards body, or, in the case of interfaces specified for a particular programming language, one that is widely used among developers working in that language.

#The “System Libraries” of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component, but which is not part of that Major Component, and (b) serves only to enable use of the work with that Major Component, or to implement a Standard Interface for which an implementation is available to the public in source code form. A “Major Component”, in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs, or a compiler used to produce the work, or an object code interpreter used to run it.

#The “Corresponding Source” for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work's System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work. For example, Corresponding Source includes interface definition files associated with source files for the work, and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work.

#The Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source.

#The Corresponding Source for a work in source code form is that same work.

#2. Basic Permissions.

#All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program. The output from running a covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law.

#You may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force. You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works, provided that you comply with the terms of this License in conveying all material for which you do not control copyright. Those thus making or running the covered works for you must do so exclusively on your behalf, under your direction and control, on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you.

#Conveying under any other circumstances is permitted solely under the conditions stated below. Sublicensing is not allowed; section 10 makes it unnecessary.

#3. Protecting Users' Legal Rights From Anti-Circumvention Law.

#No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996, or similar laws prohibiting or restricting circumvention of such measures.

#When you convey a covered work, you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work, and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work's users, your or third parties' legal rights to forbid circumvention of technological measures.

#4. Conveying Verbatim Copies.

#You may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.

#You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee.

#5. Conveying Modified Source Versions.

#You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:

#•  a) The work must carry prominent notices stating that you modified it, and giving a relevant date.

#•  b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to “keep intact all notices”.

#•  c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permission if you have separately received it.

#•  d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so.

#A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an “aggregate” if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate.

#6. Conveying Non-Source Forms.

#You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways:

#•  a) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange.

#•  b) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by a written offer, valid for at least three years and valid for as long as you offer spare parts or customer support for that product model, to give anyone who possesses the object code either (1) a copy of the Corresponding Source for all the software in the product that is covered by this License, on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or (2) access to copy the Corresponding Source from a network server at no charge.

#•  c) Convey individual copies of the object code with a copy of the written offer to provide the Corresponding Source. This alternative is allowed only occasionally and noncommercially, and only if you received the object code with such an offer, in accord with subsection 6b.

#•  d) Convey the object code by offering access from a designated place (gratis or for a charge), and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge. You need not require recipients to copy the Corresponding Source along with the object code. If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party) that supports equivalent copying facilities, provided you maintain clear directions next to the object code saying where to find the Corresponding Source. Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available for as long as needed to satisfy these requirements.

#•  e) Convey the object code using peer-to-peer transmission, provided you inform other peers where the object code and Corresponding Source of the work are being offered to the general public at no charge under subsection 6d.

#A separable portion of the object code, whose source code is excluded from the Corresponding Source as a System Library, need not be included in conveying the object code work.

#A “User Product” is either (1) a “consumer product”, which means any tangible personal property which is normally used for personal, family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling. In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage. For a particular product received by a particular user, “normally used” refers to a typical or common use of that class of product, regardless of the status of the particular user or of the way in which the particular user actually uses, or expects or is expected to use, the product. A product is a consumer product regardless of whether the product has substantial commercial, industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product.

#“Installation Information” for a User Product means any methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source. The information must suffice to ensure that the continued functioning of the modified object code is in no case prevented or interfered with solely because modification has been made.

#If you convey an object code work under this section in, or with, or specifically for use in, a User Product, and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term (regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information. But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product (for example, the work has been installed in ROM).

#The requirement to provide Installation Information does not include a requirement to continue to provide support service, warranty, or updates for a work that has been modified or installed by the recipient, or for the User Product in which it has been modified or installed. Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network.

#Corresponding Source conveyed, and Installation Information provided, in accord with this section must be in a format that is publicly documented (and with an implementation available to the public in source code form), and must require no special password or key for unpacking, reading or copying.

#7. Additional Terms.

#“Additional permissions” are terms that supplement the terms of this License by making exceptions from one or more of its conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately under those permissions, but the entire Program remains governed by this License without regard to the additional permissions.

#When you convey a copy of a covered work, you may at your option remove any additional permissions from that copy, or from any part of it. (Additional permissions may be written to require their own removal in certain cases when you modify the work.) You may place additional permissions on material, added by you to a covered work, for which you have or can give appropriate copyright permission.

#Notwithstanding any other provision of this License, for material you add to a covered work, you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:

#•  a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or

#•  b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or

#•  c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or

#•  d) Limiting the use for publicity purposes of names of licensors or authors of the material; or

#•  e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or

#•  f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material (or modified versions of it) with contractual assumptions of liability to the recipient, for any liability that these contractual assumptions directly impose on those licensors and authors.

#All other non-permissive additional terms are considered “further restrictions” within the meaning of section 10. If the Program as you received it, or any part of it, contains a notice stating that it is governed by this License along with a term that is a further restriction, you may remove that term. If a license document contains a further restriction but permits relicensing or conveying under this License, you may add to a covered work material governed by the terms of that license document, provided that the further restriction does not survive such relicensing or conveying.

#If you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms.

#Additional terms, permissive or non-permissive, may be stated in the form of a separately written license, or stated as exceptions; the above requirements apply either way.

#8. Termination.

#You may not propagate or modify a covered work except as expressly provided under this License. Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License (including any patent licenses granted under the third paragraph of section 11).

#However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation.

#Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice.

#Termination of your rights under this section does not terminate the licenses of parties who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, you do not qualify to receive new licenses for the same material under section 10.

#9. Acceptance Not Required for Having Copies.

#You are not required to accept this License in order to receive or run a copy of the Program. Ancillary propagation of a covered work occurring solely as a consequence of using peer-to-peer transmission to receive a copy likewise does not require acceptance. However, nothing other than this License grants you permission to propagate or modify any covered work. These actions infringe copyright if you do not accept this License. Therefore, by modifying or propagating a covered work, you indicate your acceptance of this License to do so.

#10. Automatic Licensing of Downstream Recipients.

#Each time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that work, subject to this License. You are not responsible for enforcing compliance by third parties with this License.

#An “entity transaction” is a transaction transferring control of an organization, or substantially all assets of one, or subdividing an organization, or merging organizations. If propagation of a covered work results from an entity transaction, each party to that transaction who receives a copy of the work also receives whatever licenses to the work the party's predecessor in interest had or could give under the previous paragraph, plus a right to possession of the Corresponding Source of the work from the predecessor in interest, if the predecessor has it or can get it with reasonable efforts.

#You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License, and you may not initiate litigation (including a cross-claim or counterclaim in a lawsuit) alleging that any patent claim is infringed by making, using, selling, offering for sale, or importing the Program or any portion of it.

#11. Patents.

#A “contributor” is a copyright holder who authorizes use under this License of the Program or a work on which the Program is based. The work thus licensed is called the contributor's “contributor version”.

#A contributor's “essential patent claims” are all patent claims owned or controlled by the contributor, whether already acquired or hereafter acquired, that would be infringed by some manner, permitted by this License, of making, using, or selling its contributor version, but do not include claims that would be infringed only as a consequence of further modification of the contributor version. For purposes of this definition, “control” includes the right to grant patent sublicenses in a manner consistent with the requirements of this License.

#Each contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor's essential patent claims, to make, use, sell, offer for sale, import and otherwise run, modify and propagate the contents of its contributor version.

#In the following three paragraphs, a “patent license” is any express agreement or commitment, however denominated, not to enforce a patent (such as an express permission to practice a patent or covenant not to sue for patent infringement). To “grant” such a patent license to a party means to make such an agreement or commitment not to enforce a patent against the party.

#If you convey a covered work, knowingly relying on a patent license, and the Corresponding Source of the work is not available for anyone to copy, free of charge and under the terms of this License, through a publicly available network server or other readily accessible means, then you must either (1) cause the Corresponding Source to be so available, or (2) arrange to deprive yourself of the benefit of the patent license for this particular work, or (3) arrange, in a manner consistent with the requirements of this License, to extend the patent license to downstream recipients. “Knowingly relying” means you have actual knowledge that, but for the patent license, your conveying the covered work in a country, or your recipient's use of the covered work in a country, would infringe one or more identifiable patents in that country that you have reason to believe are valid.

#If, pursuant to or in connection with a single transaction or arrangement, you convey, or propagate by procuring conveyance of, a covered work, and grant a patent license to some of the parties receiving the covered work authorizing them to use, propagate, modify or convey a specific copy of the covered work, then the patent license you grant is automatically extended to all recipients of the covered work and works based on it.

#A patent license is “discriminatory” if it does not include within the scope of its coverage, prohibits the exercise of, or is conditioned on the non-exercise of one or more of the rights that are specifically granted under this License. You may not convey a covered work if you are a party to an arrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work, and under which the third party grants, to any of the parties who would receive the covered work from you, a discriminatory patent license (a) in connection with copies of the covered work conveyed by you (or copies made from those copies), or (b) primarily for and in connection with specific products or compilations that contain the covered work, unless you entered into that arrangement, or that patent license was granted, prior to 28 March 2007.

#Nothing in this License shall be construed as excluding or limiting any implied license or other defenses to infringement that may otherwise be available to you under applicable patent law.

#12. No Surrender of Others' Freedom.

#If conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot convey a covered work so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not convey it at all. For example, if you agree to terms that obligate you to collect a royalty for further conveying from those to whom you convey the Program, the only way you could satisfy both those terms and this License would be to refrain entirely from conveying the Program.

#13. Use with the GNU Affero General Public License.

#Notwithstanding any other provision of this License, you have permission to link or combine any covered work with a work licensed under version 3 of the GNU Affero General Public License into a single combined work, and to convey the resulting work. The terms of this License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such.

#14. Revised Versions of this License.

#The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.

#Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License “or any later version” applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation.

#If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program.

#Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version.

#15. Disclaimer of Warranty.

#THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

#16. Limitation of Liability.

#IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

#17. Interpretation of Sections 15 and 16.

#If the disclaimer of warranty and limitation of liability provided above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee.

#END OF TERMS AND CONDITIONS

#How to Apply These Terms to Your New Programs

#If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms.

#To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the “copyright” line and a pointer to where the full notice is found.

# <one line to give the program's name and a brief idea of what it does.>

#Copyright (C) <year>  <name of author>

#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by  the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Also add information on how to contact you by electronic and paper mail.

#If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:

#<program>  Copyright (C) <year>  <name of author>

#This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.

#This is free software, and you are welcome to redistribute it under certain conditions; type `show c' for details.

#The hypothetical commands `show w' and `show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an “about box”.

#You should also get your employer (if you work as a programmer) or school, if any, to sign a “copyright disclaimer” for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>.

#The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with the library. If this is what you want to do, use the GNU Lesser General Public License instead of this License. But first, please read <http://www.gnu.org/philosophy/why-not-lgpl.html>.

#################################






# Dependencies:

import wx
import time
import os
import sys
import re
import subprocess
import shutil
from random import randint
from os.path import expanduser
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
from wx.lib.agw import ultimatelistctrl as ULC
import wx.lib.agw
import wx.html
import collections
import logging
from wx.lib.delayedresult import startWorker

app = wx.App(False)

work_dir = "/Applications"
log_name = work_dir + "/NLT.app/Contents/log.txt"
log = open(log_name, 'w')
sys.stdout = log
sys.stderr = log
command = work_dir + "/NLT.app/Contents/MacOS/bin/ffmpeg"
com = "echo $PATH"
output_name = work_dir + "/NLT.app/Contents/resultAnalyzeProducer.txt" ##
output_file = open(output_name, 'w') ##

sys.stdout.flush()

# Default settings:

TARGET_IL_DEFAULT = -24
TARGET_PEAK_DEFAULT = -2 
GRACE_DEFAULT = 2        # How far from the targetIL counts as 'within spec.'
ADJ_FILE_LOC_DEFAULT = os.getcwd()
LOG_FILE_LOC_DEFAULT = expanduser("~")
OVERWRITE_DEFAULT = True
SAME_FOLDER_DEFAULT = True
ADVANCED_ACCESS_DEFAULT = False

# OS-specific settings:

ffmpegEXE = command     # Windows: os.getcwd() + "\\FFMPEG\\bin\\ffmpeg.exe"   
SEPARATOR = '/'          # Windows: '\\' 

# Dictionary entry indices:

FILE_NAME = 0
MEETS_SPECS = 1 
INT_LOUD = 2
T_PEAK = 3
S_PEAK = 4
LOUDNESS_RANGE = 5
BITRATE = 6 
IS_RENDERED = 7
IS_ANALYZED = 8
IS_ADJUSTED = 9 
IS_MP = 10
MEETS_SPECS_ADJ = 11 
INT_LOUD_ADJ = 12
T_PEAK_ADJ = 13
S_PEAK_ADJ = 14
LOUDNESS_RANGE_ADJ = 15
IS_BAD = 16
IS_MONO = 17

# Miscellaneous Files:

LOGO_IMG = work_dir + '/NLT.app/Contents/level.png'
NPR_IMG = work_dir + '/NLT.app/Contents/npr.png'

class MainWindow(wx.Frame):
    """Build the primary window."""

    # Initialize session-specific data structures. 
    fileList = collections.OrderedDict()    # Primary file-storage data structure.
    buffer_list = []    # Stores recently deleted files.
    indexMap = []    # Maps the indices of the GUI list to the entries in fileList.

    # Specify allowed filetypes. 
    wildcard = "MP3 files (*.mp3)|*.mp3|WAV files (*.wav)|*.wav|M4A files (*.m4a)|*.m4a|AIFF files (*.aiff)|*.aiff|MP3 files (*.mp2)|*.mp2"
    allowedExtensions = ["MP3","mp3","WAV","wav","M4A","m4a","AIFF","aiff","MP2","mp2"]
    
    def __init__(self, parent, id, title):
        """Initialize and display the main GUI window."""

        wx.Frame.__init__(self, parent, id, title, size=(1000, 500))

        # Initialize settings from the configuration file and log file. 
        self.config = {}
        self.currentIndex = 1
        
        if self.currentIndex == 1:
            self.targetPeak = TARGET_PEAK_DEFAULT 
            self.targetIL = TARGET_IL_DEFAULT 
            self.grace = GRACE_DEFAULT
            self.logFileLoc = LOG_FILE_LOC_DEFAULT
            self.adjFileLoc = ADJ_FILE_LOC_DEFAULT
            self.overwrite = OVERWRITE_DEFAULT
            self.advancedAccess = ADVANCED_ACCESS_DEFAULT
            self.sameFold = SAME_FOLDER_DEFAULT

#        else:
 
        # Construct horizontal menu bar.
        menubar = wx.MenuBar()
        about = wx.Menu()

        toolInfoItem = about.Append(wx.NewId(), '&NPR Loudness Tool', 'Information about the NPR Loudness Tool')
        self.Bind(wx.EVT_MENU, self.OnToolInfo, toolInfoItem)  

        licInfoItem = about.Append(wx.NewId(), '&License', 'Information about the License')
        self.Bind(wx.EVT_MENU, self.OnLicInfo, licInfoItem)  

        standInfoItem = about.Append(wx.NewId(), '&Loudness Standards', 'Information about the Loudness Standards')
        self.Bind(wx.EVT_MENU, self.OnStandInfo, standInfoItem)  

        labsInfoItem = about.Append(wx.NewId(), '&NPR Labs', 'Information about NPR Labs')
        self.Bind(wx.EVT_MENU, self.OnLabsInfo, labsInfoItem)  

        helpInfoItem = about.Append(wx.NewId(), '&Help', 'Where to get more help')
        self.Bind(wx.EVT_MENU, self.OnHelpInfo, helpInfoItem)  

        gplInfoItem = about.Append(wx.NewId(), '&GNU GPL', 'GNU GENERAL PUBLIC LICENSE')
        self.Bind(wx.EVT_MENU, self.OnGPLInfo, gplInfoItem)  
        
        menubar.Append(about, '&More')

        self.SetMenuBar(menubar)

        # Add internal structure to the main frame.
        panel = wx.Panel(self, -1)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        buttonPanel = wx.Panel(panel, -1)
        filePanel = wx.Panel(panel, -1)

        # Construct the GUI's underlying file list.

        self.list = ULC.UltimateListCtrl(filePanel, agwStyle = wx.LC_REPORT | wx.LC_VRULES )
        self.list.InsertColumn(0, ' ', width=20)
        self.list.InsertColumn(1, 'Filename', wx.LIST_FORMAT_LEFT, width=300)
        self.list.InsertColumn(2, 'Progress', wx.LIST_FORMAT_CENTER, width=100)
        self.list.InsertColumn(3, 'Meets Specs?', wx.LIST_FORMAT_CENTER, width=100)
        self.list.InsertColumn(4, 'Integrated Loudness', wx.LIST_FORMAT_CENTER, width=130)
        self.list.InsertColumn(5, 'True Peak', wx.LIST_FORMAT_CENTER, width=100)
        self.list.InsertColumn(6, 'Peak Value', wx.LIST_FORMAT_CENTER, width=100)

        # Establish file list as a drag-and-drop target.
        dropTarget = FileDrop(self.list, self)
        self.list.SetDropTarget(dropTarget)

        # Populate the button panel.
        self.loadfile = wx.Button(buttonPanel, -1, 'Upload File', size=(100, -1))
        self.loadfolder = wx.Button(buttonPanel, -1, 'Upload Folder', size=(100, -1))
        self.sel = wx.Button(buttonPanel, -1, 'Select All', size=(100, -1))
        self.sel.Disable()
        self.des = wx.Button(buttonPanel, -1, 'Deselect All', size=(100, -1))
        self.des.Disable()
        self.ana = wx.Button(buttonPanel, -1, 'Analyze', size=(100, -1))
        self.ana.Disable()
        self.adj = wx.Button(buttonPanel, -1, 'Adjust', size=(100, -1))
        self.adj.Disable()

        # Add logo.
        img = wx.Image(LOGO_IMG, wx.BITMAP_TYPE_ANY)
        w = img.GetWidth()
        h = img.GetHeight()
        img_scaled = img.Scale(w/1, h/1) ##
        self.logo = wx.StaticBitmap(buttonPanel, -1, wx.BitmapFromImage(img_scaled))

        # Bind buttons to their respective functions.
        self.Bind(wx.EVT_BUTTON, self.OnLoadFile, id=self.loadfile.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnLoadFolder, id=self.loadfolder.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnSelectAll, id=self.sel.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDeselectAll, id=self.des.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnAnalyze, id=self.ana.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnAdjust, id=self.adj.GetId())

        # Add NPR logo and copyright message.
        wmark = wx.Image(NPR_IMG, wx.BITMAP_TYPE_ANY)
        w = wmark.GetWidth()
        h = wmark.GetHeight()
        wmark_scaled = wmark.Scale(w/1, h/1) ##
        self.watermark = wx.StaticBitmap(filePanel, -1, wx.BitmapFromImage(wmark_scaled))
        self.copyright = wx.StaticText(filePanel, -1, "Copyright 2016 NPR")

        # Set sizers.
        vbox1.Add(self.list, 1, wx.EXPAND | wx.TOP, 3)
        vbox1.Add((-1, 10))
        vbox1.Add(self.watermark,0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTRE | wx.SHAPED)       
        vbox1.Add(self.copyright, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTRE)
        filePanel.SetSizer(vbox1)

        vbox2.Add(self.logo, 0, wx.ALL, 10)
        vbox2.Add(self.loadfile, 0, wx.ALL, 10)
        vbox2.Add(self.loadfolder, 0, wx.ALL, 10)
        vbox2.Add(self.sel, 0, wx.ALL, 10)
        vbox2.Add(self.des, 0, wx.ALL, 10)
        #vbox2.Add(self.rem, 0, wx.ALL, 10)
        #vbox2.Add(self.und, 0, wx.ALL, 10)    # Disabled until applicable
        vbox2.Add(self.ana, 0, wx.ALL, 10)
        vbox2.Add(self.adj, 0, wx.ALL, 10)
        buttonPanel.SetSizer(vbox2)
  
        hbox.Add(buttonPanel, 0, wx.EXPAND | wx.RIGHT, 5)
        hbox.Add(filePanel, 1, wx.EXPAND)
        hbox.Add((3, -1))
        panel.SetSizer(hbox)

        # Initialize log file.
        logfilepath = self.logFileLoc + SEPARATOR + "logfile.txt" 
        if os.path.exists(logfilepath):
            self.logfile = open(logfilepath, 'a+')
        else:
            try: 
                self.logfile = open(logfilepath, 'w+')
            except:
                pass

        # Center and display main frame.
        self.Centre()
        self.Show(True)

    def OnQuit(self, event):
        self.Close()

    def OnInfo(self, event):
        """Launch a window that provides information."""
        dlg = InfoDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnToolInfo(self, event):
        """Launch a window that provides information."""
        dlg = ToolInfoDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnLicInfo(self, event):
        """Launch a window that provides information."""
        dlg = LicInfoDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnStandInfo(self, event):
        """Launch a window that provides information."""
        dlg = StandInfoDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnLabsInfo(self, event):
        """Launch a window that provides information."""
        dlg = LabsInfoDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnHelpInfo(self, event):
        """Launch a window that provides information."""
        dlg = HelpInfoDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnGPLInfo(self, event):
        """Launch a window that provides information."""
        dlg = GPLInfoDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnBadInput(self, file):
        """Notify the user of any invalid inputs."""
        self.fileList[file][IS_ANALYZED] = True
        self.fileList[file][IS_ADJUSTED] = True
        self.fileList[file][IS_BAD] = True
        message = wx.StaticText(self.panel, id=-1,style=wx.ALIGN_CENTRE, label="ffmpeg detected bad input for %s; check the extension on your file and ensure that your data has not been corrupted." % file)
        dlg = wx.MessageDialog(self, "Bad Input", message, style=wx.OK|wx.ICON_EXCLAMATION)
        dlg.ShowModal()

    def OnAnalyze(self, event):
        """The event handler for the 'Analyze' button."""
        # Calls the AnalyzeHelper method with the argument 'False' to indicate that
        # the 'Adjust' button has not also been triggered.
        self.AnalyzeHelper(False)

    def AnalyzeHelper(self, toAdjustLater):
        """Call an analysis thread for every selected item."""
        # Populate a list of selected files to be analyzed (ignoring any that have already been analyzed).
        toAnalyze = [] 

        for i in range(self.list.GetItemCount()):
            if i%3 == 0:    # Change this value to i%2 if you decide to get rid of the spacer 
                           # line (and do likewise where appropriate throughout the file).
              check = self.list.GetItem(i,0)
              box = check.GetWindow()
              file = self.indexMap[i/3]
              if box.GetValue() and not self.fileList[file][IS_ANALYZED]:
                toAnalyze.append((file,i))

        

        # Launch an analysis thread and progress bar for each selected file.
        for (file,index) in toAnalyze:
            item = self.list.GetItem(index,2)
            gauge = item.GetWindow()
            gauge.Pulse()
            self._resultAnalyzeProducer(file, index) 
           
        # If the call to 'AnalyzeHelper' was initiated by pressing the 'Adjust' button, 
        # proceed to the AdjustHelper function. 
        if toAdjustLater:
            self.AdjustHelper()

    def OnAdjust(self, event):
        """The event handler for the 'Adjust' button."""
        # Initiate analysis, while flagging files for post-analysis adjustment. 
        self.AnalyzeHelper(True)
                
    def AdjustHelper(self):
        """Call an adjust thread for every selected item."""
        # Compile list of selected files (ignoring any that have already been adjusted).
        toAdjust = []

        for i in range(self.list.GetItemCount()):
           if i%3 == 0:
               check = self.list.GetItem(i,0)
               box = check.GetWindow()
               file = self.indexMap[i/3]
               if box.GetValue() and not self.fileList[file][IS_ADJUSTED]:
                   toAdjust.append((file,i+1))

        # Perform adjustment for each selected item. 
        for (file,index) in toAdjust:
            

            # Add progress bars.
            item = self.list.GetItem(index,2)
            item._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_FONTCOLOUR
            width = self.list.GetColumnWidth(1)
            gauge = wx.Gauge(self.list,-1,range=50,size=(width,15),style=wx.GA_HORIZONTAL | wx.GA_SMOOTH)
            gauge.Pulse() #shouldn't start this right away...
            item.SetWindow(gauge, wx.ALIGN_CENTRE)
            self.list.SetItem(item) 

            # Display the names of the to-be-adjusted files.
            (dir,just_file) = os.path.split(os.path.abspath(file))
            file_name_as_string = str(just_file)
            dot = re.search("(.*\.)*(.*)", file_name_as_string)
            extension = dot.group(2)
            
            n = re.search(extension, file_name_as_string)
            stem = file_name_as_string[:n.start()-1]

            timestamp = time.strftime("%d-%m-%Y;%H%M") + '.'
            if not self.overwrite:
                adjusted_file = stem + "_adjusted_" + timestamp + extension
            else: 
                adjusted_file = stem + "_adjusted." + extension
            self.list.SetStringItem(index, 1, adjusted_file) 

            # Launch an adjust thread for each selected file.
            self._resultAdjustProducer(file, timestamp, index)

            # Once adjustment has been performed, uncheck the box and set the 'adjusted' field to True.
            self.fileList[file][IS_ADJUSTED] = True 
            check = self.list.GetItem(index-1,0)
            box = check.GetWindow()
            box.SetValue(False)

        """Invoke the ffmpeg analysis routine and pipe the output to self._resultAnalyzeConsumer."""

    def _resultAnalyzeProducer(self, file, index):
        
        output_name = work_dir + "/NLT.app/Contents/resultAnalyzeProducer.txt" 
        output_file = open(output_name, 'w') 
        proc = subprocess.call([ffmpegEXE, '-nostats', '-i', file, '-filter_complex', 'ebur128=peak=true+sample:framelog=verbose', '-f', 'null', '-'], bufsize=1, stdout=output_file, stderr=output_file)

        sys.stdout.flush()
        
        buffered = open(output_name, 'rU').read()
        sys.stdout.flush()

        self.prologue = buffered.split('Press [q]')[0]    # Capture the beginning of the output information (which includes bitrate).

        
##test mono v. stereo

        channels = re.search(r'Hz, (.+?),', self.prologue)
        chVal = channels.group(1)
        

        if ((chVal == "mono") or (chVal == "1 channels")):
            self.fileList[file][IS_MONO] = True
            self.targetIL = -27
            
## put mono stuff back in here ##

        if ((chVal == "stereo") or (chVal == "2 channels")):
            self.fileList[file][IS_MONO] = False
            self.targetIL = -24

        if not ((chVal == "mono") or (chVal == "1 channels") or (chVal == "stereo") or (chVal == "2 channels")):
            self.fileList[file][IS_MONO] = False
            self.targetIL = -24
        split_part = buffered.partition('Summary:\n')
        self.summary = str(split_part[2])
        result = self.prologue + ''.join(self.summary)    # Return both for processing. 

        item = self.list.GetItem(index,2)
        gauge = item.GetWindow()
        gauge.SetValue(50)

        # Catch bad inputs and inform the user.
        badInput = re.search(r'Invalid data found when processing input', result) #will it get here without error?
        if badInput is not None:
            wx.CallAfter(self.OnBadInput,file)
        else:
            self.ProcessSummary(file, result, index)
        ##    
        
        
    def ProcessSummary(self, file, summary, i):
        """Process ffmpeg data and display it in the GUI."""
        errorFlag = False

        # Extract bitrate. 
        if not self.fileList[file][IS_ANALYZED]:
            bitrate = re.search(r'bitrate:\s(.+?) kb', summary) #changed from summary
            if bitrate is not None:
                BR = bitrate.group(1)
            else:
                BR = "n/a"
                errorFlag = True         
            self.fileList[file][BITRATE] = BR

        # Extract loudness range.
        #loudnessRange = re.search(r'LRA:\s(.+?) LU', summary)
        #if loudnessRange is not None:
        #    LRA = loudnessRange.group(1)
        #else:
        #    LRA = "n/a"
        #    errorFlag = True
        #self.list.SetStringItem(i,7,LRA)         
        #if i%3 == 0:
        #    self.fileList[file][LOUDNESS_RANGE] = LRA
        #else:
        #    self.fileList[file][LOUDNESS_RANGE_ADJ] = LRA

        # Extract integrated loudness. 

        intloud = re.search(r'I:\s*(.+?) LUFS', summary)
        full_thing = intloud.group(0)
        if intloud is not None:
            IL = intloud.group(1)
        else:
            IL = "n/a"
            errorFlag = True

        if self.fileList[file][IS_MONO] == True:
            ILint = float(IL)
            ILtoShow = str(ILint + 3)
        else:
            ILtoShow = IL
            
        
        self.list.SetStringItem(i,4,ILtoShow)

        if i%3 == 0:
            self.fileList[file][INT_LOUD] = IL
        else:
            self.fileList[file][INT_LOUD_ADJ] = IL

        truePeak = re.search(r'True peak:\s+Peak:\s+(.+?) dBFS', summary)

        if truePeak is not None:
            TP = truePeak.group(1)
        else:
            TP = "n/a"
            errorFlag = True
        self.list.SetStringItem(i,5,TP)

        if i%3 == 0:
            self.fileList[file][T_PEAK] = TP
        else:
            self.fileList[file][T_PEAK_ADJ] = IL

        # Extract sample peak.
        samplePeak = re.search(r'Sample peak:\s*Peak:\s*(.+?) dBFS', summary)

        if samplePeak is not None:
            SP = samplePeak.group(1)
        else:
            SP = "n/a"
            errorFlag = True
        self.list.SetStringItem(i,6,SP)
        if i%3 == 0:
            self.fileList[file][S_PEAK] = SP
        else:
            self.fileList[file][S_PEAK_ADJ] = IL

        # Append time-stamped data to log file. 
        self.logfile.write(file)
        if i%3 == 1:
            self.logfile.write(" (adjusted)")
        if errorFlag:
            self.logfile.write("\nThis process was aborted prematurely.")
        #self.logfile.write("LRA: " + str(LRA) + "\n\n\n")
        
        ##

        ##
        # Notify users of any data-collection errors; if no errors are detected, flag the file as analyzed.
        if errorFlag:
            self.list.SetStringItem(i,3,"Error")
        else:
            self.fileList[file][IS_ANALYZED] = True

        # Determine whether the file conforms to specs.
        upperbound = self.targetIL + self.grace 
        lowerbound = self.targetIL - self.grace 

        if float(IL) > lowerbound and float(IL) < upperbound:
            valid = True
        else:
            valid = False
        if float(truePeak.group(1)) > self.targetPeak:
            valid = False

        # Notify the GUI of whether the file meets specs.
        if valid:
            self.list.SetStringItem(i,3,"Yes")
            item = self.list.GetItem(i,3)
            item.SetTextColour(wx.GREEN)    
            self.list.SetItem(item)
            if i%3 == 0:
                self.fileList[file][MEETS_SPECS] = "Yes"
                check = self.list.GetItem(i,0)
                box = check.GetWindow()
#                box.SetValue(False)
 #               self.list.SetItem(check)
            else:
                self.fileList[file][MEETS_SPECS_ADJ] = "Yes"
        else:
            self.list.SetStringItem(i,3,"No")
            if i%3 == 0:
                self.fileList[file][MEETS_SPECS] = "No"
            else:
                self.fileList[file][MEETS_SPECS_ADJ] = "No"
 
    def _resultAdjustProducer(self, file, timestamp, index):
        """Invoke the ffmpeg adjust routine and pipe the output to __resultAdjustConsumer."""
 

        if self.fileList[file][IS_MONO] == True:
            self.targetIL = -27
        else:
            self.targetIL = -24
        
        output_name = work_dir + "/NLT.app/Contents/output_file_resultAdjustProducer.txt" ##

        output_name_second = work_dir + "/NLT.app/Contents/output_file_resultAdjustProducer_second.txt" ##

        file_name_as_string = str(file)

        dot = re.search("(.*\.)*(.*)", file_name_as_string)
        extension = dot.group(2)
            
        # Specify path of adjusted file based on config settings.
        (dir,just_file) = os.path.split(os.path.abspath(file))
        if not self.sameFold:
            dir = self.adjFileLoc
            fileNewFold = dir + SEPARATOR + just_file   
        else:
            fileNewFold = file
        
        type(fileNewFold)

        fileNewFold_str = str(fileNewFold)

        dot = re.search("(.*\.)*(.*)", fileNewFold_str)
 
        # Convert mp3 files to wav before processing.
        
        n = re.search(extension, fileNewFold_str)

        stem = fileNewFold_str[:n.start() - 1]

        if ((extension == "mp3") or (extension == "mp2")):
            old_ext = extension

            self.fileList[file][IS_MP] = True    
            extension = "wav"

#            wav_file = fileNewFold[:dot.start()] + '.' + extension    # Name equivalent wav file.#
            wav_file = stem + '.' + extension    # Name equivalent wav file.#

            if os.path.isfile(wav_file):    # Remove any existing files of that name.
                os.remove(wav_file)
            output_file = open(output_name, 'w') ##proc = subprocess.call([ffmpegEXE, '-i', file, wav_file], bufsize = 1, stdout=output_file, stderr=output_file)
            sys.stdout.flush()
            output_file.close()
            adjusted_MP = stem + "_adjusted." + old_ext    # Name final adjusted MP3 file.
            if os.path.isfile(adjusted_MP):    # Remove any existing files of that name.
                os.remove(adjusted_MP)

        # Define other helper files and remove any duplicates (i.e. permit overwrites). 
        ## overwriting ##
        #
        if self.overwrite:  

            start_file = stem + "_start." + extension
            intermed_file = stem + "_intermed." + extension
            adjusted_file = stem + "_adjusted." + extension   

        else:
            start_file = stem + "_start_" + timestamp + extension
            intermed_file = stem + "_intermed_" + timestamp + extension
            adjusted_file = stem + "_adjusted_" + timestamp + extension 

        if os.path.isfile(start_file):
            os.remove(start_file) 
        if os.path.isfile(adjusted_file):
            os.remove(adjusted_file) 
        if os.path.isfile(intermed_file):
            os.remove(intermed_file)

        # Copy the original file to `start_file' to prevent modification of the original.
        shutil.copy(file, start_file) 

        # Calculate gain shift and target peak.
        IL = float(self.fileList[file][INT_LOUD])
        TP = float(self.fileList[file][T_PEAK])
        gain = self.targetIL - IL
        newTruePeak = TP + gain

        # Branch 1: integrated loudness is too low, upward gain shift required.
        if gain > 0:
        # Perform up to five extra rounds of gain shifting, to "nudge" finnicky files to the target value.
            count = 0
            direction = [False,False] #added by alice
            while (count < 5):
                # Branch 1A: no compression required, simply gain shift.
                if newTruePeak < self.targetPeak: 
                    output_file = open(output_name_second, 'w') ##
                    proc = subprocess.call([ffmpegEXE, '-i', start_file, '-strict', '-2', '-af', 'volume=volume=' + str(gain) + 'dB:precision=fixed',  adjusted_file], bufsize=1, stdout=output_file, stderr=output_file)
                    
                    #stdout,stderr = proc.communicate() 
                    sys.stdout.flush()
                    output_file.close()
                # Branch 1B: begin iterative compression and gain shift.
                else:
                    j = 0
                    while (newTruePeak > self.targetPeak) and j < 4:    # Forestall infinite loops.
                        # Perform round of compression.
                        offset = self.targetPeak - gain

                        output_file = open(output_name, 'w') ##
                        proc = subprocess.call([ffmpegEXE, '-i', start_file, '-strict', '-2', '-af', 'compand=.00001:.5:-90/-90|-40/-40|-30/-30|-20/-20|-10/-10|-8/-8' + str(offset) + '/' + str(offset - 2) + '|-3/' + str(offset - 1) + '|-1/' + str(offset - 0.1) + '|0/' + str(offset) + ':0.01:0:0:0.01', intermed_file], bufsize=1, stdout=output_file, stderr=output_file)
                        sys.stdout.flush()
                        output_file.close()

                        # Analyze the resulting file.
#                        proc  = subprocess.Popen([ffmpegEXE, '-nostats', '-i', intermed_file, '-filter_complex', 'ebur128=peak=true+sample', '-f', 'null', '-'], bufsize=1, stdout=output_file, stderr=output_file)
#                        #stdout,stderr = proc.communicate()

                        output_file = open(output_name_second, 'w') ##
                        proc  = subprocess.call([ffmpegEXE, '-nostats', '-i', intermed_file, '-filter_complex', 'ebur128=peak=true+sample:framelog=verbose', '-f', 'null', '-'], bufsize=1, stdout=output_file, stderr=output_file)
                        sys.stdout.flush()
                        output_file.close()

                        buffered = open(output_name_second, 'rU').read() ##
                        split_part = buffered.partition('Summary:\n')
                        self.summary = str(split_part[2])
                        
                        intloud = re.search(r'I:(.+?) LUFS',self.summary)
                        intL = intloud.group(1)

                        if intloud is not None:
                            intloud = float(intloud.group(1))
                            gain = self.targetIL - intloud
                        ##if intloud == None:
                        
                        truePeak = re.search(r'True peak:\s+Peak:\s(.+?) dBFS',self.summary)
                        if truePeak is not None:
                            truePeak = float(truePeak.group(1))
                        #if truePeak == None:
                        
                        # Perform requisite gain shift.
                        
                        output_file = open(output_name, 'w')

                        newGain = self.targetIL - intloud
                        proc = subprocess.call([ffmpegEXE, '-i', intermed_file, '-strict', '-2', '-af', 'volume=volume=' + str(newGain) + 'dB:precision=fixed',  adjusted_file], bufsize=1, stdout=output_file, stderr=output_file)
                        sys.stdout.flush()
                        output_file.close()
    #Now here we're doing that extra round of analysis...
                        #stdout,stderr = proc.communicate()

                        # Analyze the resulting file (MAKE THIS A SEPARATE HELPER METHOD).
                        output_file = open(output_name, 'w') ##
                        proc  = subprocess.call([ffmpegEXE, '-nostats', '-i', adjusted_file, '-filter_complex', 'ebur128=peak=true+sample:framelog=verbose', '-f', 'null', '-'], bufsize=1, stdout=output_file, stderr=output_file)
                        sys.stdout.flush()
                        output_file.close()
                        #stdout,stderr = proc.communicate()
        #
                        #output_file = open(output_name, 'w') ##
                        buffered = open(output_name, 'rU').read() ##made it = rather than +=

                        split_part = buffered.partition('Summary:\n')
                        summary = str(split_part[2])
 
                        intloud = re.search(r'I:\s(.+?) LUFS', summary)
                        if intloud is not None:
                            intloud = float(intloud.group(1))
                        gain = self.targetIL - intloud

                        truePeak = re.search(r'True peak:\s+Peak:\s(.+?) dBFS', summary)
                        if truePeak is not None:
                            truePeak = float(truePeak.group(1))

                        # Calculate new true peak and rename files accordingly.
                        newTruePeak = truePeak
                        os.rename(adjusted_file, start_file) 
                        if os.path.isfile(intermed_file):
                            os.remove(intermed_file)

                        j += 1

                    os.rename(start_file, adjusted_file)

                # Process the output.
                output_file = open(output_name, 'w') ##
                proc = subprocess.call([ffmpegEXE, '-nostats', '-i', adjusted_file, '-filter_complex', 'ebur128=peak=true+sample:framelog=verbose', '-f', 'null', '-'], bufsize=1, stdout=output_file, stderr=output_file)
                #stdout,stderr = proc.communicate()
                sys.stdout.flush()
                output_file.close()
                buffered = open(output_name, 'rU').read() ##made it = rather than +=
                #filePath.close()

                split_part = buffered.partition('Summary:\n')
                summary = str(split_part[2])

                intloud = re.search(r'I:\s(.+?) LUFS', summary)

                gainDiff = 0 ##
                
                if intloud is not None:
                    intloud = float(intloud.group(1))
                    gainDiff = self.targetIL - intloud

                if gainDiff == 0:
                    break
                else:
                    if gainDiff < 0:
                        direction[0] = True
                    else:
                        direction[1] = True
                    count += 1
                    if direction[0] and direction[1]:
                        gainDiff = gainDiff/3.0
                    gain = gain + gainDiff
                    if os.path.isfile(intermed_file):
                        os.remove(intermed_file)
                    if count == 4 and os.path.isfile(adjusted_file):
                        os.remove(adjusted_file)

        # Branch 2: integrated loudness is too high, downward gain shift required.
        else:
        # Perform up to five extra rounds of gain shifting, to "nudge" finnicky files to the target value.
            count = 0
            direction = [False,False]
            while (count < 5):
                # Perform downward gain shift.
                output_file = open(output_name, 'w') ##
                proc = subprocess.call([ffmpegEXE, '-i', start_file, '-strict', '-2', '-af', 'volume=volume=' + str(gain) + 'dB:precision=fixed',  intermed_file], bufsize=1, stdout=output_file, stderr=output_file)
                sys.stdout.flush()
                output_file.close()
                #stdout,stderr = proc.communicate()

                # Branch 2A: Perform compression if required. 
                if newTruePeak > self.targetPeak: #but... that actually will never be the case, right??
                    output_file = open(output_name, 'w') ##
                    proc2 = subprocess.call([ffmpegEXE, '-i', intermed_file, '-strict', '-2', '-af', 'compand=.00001|.00001:.5|.5:-90/-90|-4/-4|-3.2/-3.3|-3.1/-3.2|0/-3.1:0.01:0:0:0.01', adjusted_file], bufsize=1, stdout=output_file, stderr=output_file)
                    sys.stdout.flush()
                    output_file.close()
                    #stdout, stderr = proc2.communicate() 

                # Branch 2B: Otherwise, change file names accordingly.
                else:
                    ##os.remove(adjusted_file)
                    os.rename(intermed_file, adjusted_file)

                # Process the output.
                output_file = open(output_name, 'w') ##
                proc = subprocess.call([ffmpegEXE, '-nostats', '-i', adjusted_file, '-filter_complex', 'ebur128=peak=true+sample:framelog=verbose', '-f', 'null', '-'], bufsize=1, stdout=output_file, stderr=output_file)
                sys.stdout.flush()
                output_file.close()
                
                buffered = open(output_name, 'rU').read() ##made it = rather than +=
                
                split_part = buffered.partition('Summary:\n')
                summary = str(split_part[2])
 

                intloud = re.search(r'I:\s(.+?) LUFS', summary)
                if intloud is not None:
                    intloud = float(intloud.group(1))
                    gainDiff = self.targetIL - intloud

                if gainDiff == 0:
                    break
                else:
                    if gainDiff < 0:
                        direction[0] = True
                    else:
                        direction[1] = True
                    count += 1
                    if direction[0] and direction[1]:
                        gainDiff = gainDiff/2.0
                    gain = gain + gainDiff
                    if os.path.isfile(intermed_file):
                        os.remove(intermed_file)
                    if count == 4 and os.path.isfile(adjusted_file):
                        os.remove(adjusted_file)

 
        # Analyze output.
        
        output_file = open(output_name, 'w') 
        proc = subprocess.call([ffmpegEXE, '-nostats', '-i', adjusted_file, '-filter_complex', 'ebur128=peak=true+sample:framelog=verbose', '-f', 'null', '-'], bufsize=1, stdout=output_file, stderr=output_file)
        sys.stdout.flush()
        output_file.close()
        
        buffered = open(output_name, 'rU').read() 
        
        split_part = buffered.partition('Summary:\n')
        summary = str(split_part[2])
 
    
        intloud = re.search(r'I:\s(.+?) LUFS', summary)
        if intloud is not None:
            intloud = float(intloud.group(1))
            gain = self.targetIL - intloud

        if self.fileList[file][IS_MP]:
            bitrateParam = self.GetBitrateParam(self.fileList[file][BITRATE])
            output_file = open(output_name, 'w')
            if (abs(bitrateParam - 128) < 10):
                bitrateParam = 128
            if (abs(bitrateParam - 256) < 10):
                bitrateParam = 256

            br_to_use = str(bitrateParam) + 'k'
            proc = subprocess.call([ffmpegEXE,'-i', adjusted_file, '-b:a', br_to_use, adjusted_MP])
            sys.stdout.flush()
            output_file.close()

            output_file = open(output_name, 'w')
            proc = subprocess.call([ffmpegEXE, '-nostats', '-analyzeduration', '2147483647', '-probesize', '2147483647', '-i', adjusted_MP, '-filter_complex', 'ebur128=peak=true+sample:framelog=verbose', '-f', 'null', '-'], bufsize=1, stdout=output_file, stderr=output_file)
            sys.stdout.flush()
            output_file.close()
            if os.path.isfile(adjusted_file):
                os.remove(adjusted_file)

        else:          
            output_file = open(output_name, 'w')
            proc = subprocess.call([ffmpegEXE, '-nostats', '-i', adjusted_file, '-filter_complex', 'ebur128=peak=true+sample:framelog=verbose', '-f', 'null', '-'], bufsize=1, stdout=output_file, stderr=output_file)
            sys.stdout.flush()
            output_file.close()

        buffered = open(output_name, 'rU').read()

        split_part = buffered.partition('Summary:\n')
        self.summary = str(split_part[2])
 
        # Clean up any loose files. 
        if os.path.isfile(start_file):
            os.remove(start_file)
        if os.path.isfile(intermed_file):
            os.remove(intermed_file)
        if self.fileList[file][IS_MP]:  #(OMW: Check to make sure this doesn't break anything!!)
            if os.path.isfile(wav_file):
                os.remove(wav_file)

        result = ''.join(self.summary)
        self.ProcessSummary(file, result, index) 
        item = self.list.GetItem(index,2)
        gauge = item.GetWindow()
        gauge.SetValue(50)
        
    def GetBitrateParam(self, bitrate):
        """Convert bitrate to the appropriate libmp3lame parameter. (Note that for boundary cases, 
           we have chosen to air on the side of a higher bitrate. https://trac.ffmpeg.org/wiki/Encode/MP3)"""
        
        bitrateString = bitrate
        bitrate = int(bitrateString)
        return bitrate

    def OnLoadFile(self, event):
       """Load a file selection dialog."""
       dlg = wx.FileDialog(self, "Choose a file:", os.getcwd(), "", "*.*", wx.OPEN | wx.FD_MULTIPLE)
       dlg.SetWildcard(self.wildcard)     # Establish allowed file types.
       if dlg.ShowModal() == wx.ID_OK:
           for file in dlg.GetPaths():
               self.AddToList(file)
       dlg.Destroy()
       self.Render()

    def OnLoadFolder(self, event):
       """Load a folder selecton dialog."""

       dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
       if dlg.ShowModal() == wx.ID_OK:
           path = dlg.GetPath()
           for file in os.listdir(path):
               self.AddToList(path + SEPARATOR + file)   # Separator depends on the OS. 
       dlg.Destroy()
       self.Render()

    def AddToList(self, file):
       """Add a file to the queue."""

       # Isolate the file extension.
       rawfilename = os.path.basename(file)
       dot = re.search("\.(?=[^.]*$)",rawfilename)
       if dot:
          extension = rawfilename[dot.end():]
       else:
          extension = "dummyExt"    # 

       # Add files that have an appropriate extension and have not been previously added.
       if not file in self.fileList and extension in self.allowedExtensions:

          self.fileList[file] = [file,'','','','','','',False,False,False,False,'','','','','',False, False] 
 
    def Render(self):
       """Display file list."""

       # If the file list is not empty, enable buttons.
       if self.fileList:
          self.sel.Enable()
          self.des.Enable()
          #self.rem.Enable()
          self.ana.Enable()
          self.adj.Enable()

       # Add file to the window if it hasn't been previously rendered.   
       for file in self.fileList:
          entry = self.fileList[file]

          if not entry[IS_RENDERED]:  
             index = self.list.InsertStringItem(sys.maxint, '')
             (dir,just_file) = os.path.split(os.path.abspath(file))
             self.list.SetStringItem(index, 1, just_file)
             self.list.SetStringItem(index, 3, entry[MEETS_SPECS])
             posit = self.list.GetItemPosition(index)
             self.list.SetStringItem(index, 4, entry[INT_LOUD])
             self.list.SetStringItem(index, 5, entry[T_PEAK])
             self.list.SetStringItem(index, 6, entry[S_PEAK])
             #self.list.SetStringItem(index, 7, entry[LOUDNESS_RANGE])
       
             # Insert and automatically select checkboxes.
             check = self.list.GetItem(index,0)
             box = wx.CheckBox(self.list, -1, size=(20,20),pos=posit)   # The checkbox needed to be forced to a reasonable location. 
             if entry[IS_ADJUSTED]: 
                 box.SetValue(False)
             else:
                 box.SetValue(True)
             check.SetWindow(box, wx.ALIGN_CENTRE)
             self.list.SetItem(check)

             # Insert progress bars (initialized to zero). 
             item = self.list.GetItem(index,2)
             item._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_FONTCOLOUR
             width = self.list.GetColumnWidth(1)
             self.gauge = wx.Gauge(self.list,-1,range=50,size=(width,15),style=wx.GA_HORIZONTAL | wx.GA_SMOOTH)
             if entry[IS_ANALYZED]:
                 self.gauge.SetValue(50)
             else:
                 self.gauge.SetValue(0)
             item.SetWindow(self.gauge, wx.ALIGN_CENTRE)
             self.list.SetItem(item) 

             # Leave two spaces between each entry for adjustment and readability.
             adjustrow = self.list.InsertStringItem(sys.maxint, '')   
             if entry[IS_ADJUSTED]:
                 dot = re.search("\.", just_file)
                 extension = just_file[dot.end():]
                 adjusted_file = just_file[:dot.end()-1] + "_adjusted." + extension
                 self.list.SetStringItem(adjustrow, 1, adjusted_file)
                 self.list.SetStringItem(adjustrow, 3, entry[MEETS_SPECS_ADJ])
                 self.list.SetStringItem(adjustrow, 4, entry[INT_LOUD_ADJ])
                 self.list.SetStringItem(adjustrow, 5, entry[T_PEAK_ADJ])
                 self.list.SetStringItem(adjustrow, 6, entry[S_PEAK_ADJ])
                 self.list.SetStringItem(adjustrow, 7, entry[LOUDNESS_RANGE_ADJ])

                 item = self.list.GetItem(adjustrow,2)
                 item._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_FONTCOLOUR
                 width = self.list.GetColumnWidth(1)
                 self.gauge = wx.Gauge(self.list,-1,range=50,size=(width,15),style=wx.GA_HORIZONTAL | wx.GA_SMOOTH)
                 self.gauge.SetValue(50)
                 item.SetWindow(self.gauge, wx.ALIGN_CENTRE)
                 self.list.SetItem(item) 

             
             self.list.InsertStringItem(sys.maxint, '')
             entry[IS_RENDERED] = True     # Flag the file as rendered

       self.UpdateIndexMap()

    def UpdateIndexMap(self):
        """Reset the index map to reflect any newly added files."""

        self.indexMap = []
        for file in self.fileList:
            self.indexMap.append(file) 

    def OnSelectAll(self, event):
        """Check all boxes in the file list."""

        num = self.list.GetItemCount()
        for i in range(num):
            if i%3 == 0:
                check = self.list.GetItem(i,0)
                box = check.GetWindow()
                box.SetValue(True)
                self.list.SetItem(check)
           

    def OnDeselectAll(self, event):
        """Uncheck all boxes in the file list."""

        num = self.list.GetItemCount()
        for i in range(num):
            if i%3 == 0:
                check = self.list.GetItem(i,0)
                box = check.GetWindow()
                box.SetValue(False)
                self.list.SetItem(check)

    def OnRemove(self, event):
        """Remove selected files from the file list."""

        toDelete = []
        self.buffer_list = []    # Store recently deleted files
        num = self.list.GetItemCount()

        # Compile list of files selected for deletion. 
        for i in range(num):
           if i%3 == 0:
              check = self.list.GetItem(i,0)
              box = check.GetWindow()           
              if box.GetValue():
                 toDelete.append(self.indexMap[i/3])
              self.fileList[self.indexMap[i/3]][IS_RENDERED] = False 
              
        # Pop files from the fileList (adding them to a buffer for safe-keeping) and re-render. 
        for name in toDelete:
           self.buffer_list.append(self.fileList.pop(name))
        self.list.DeleteAllItems()
        self.Render()
        self.und.Enable() 
 
        
    def OnUndo(self, event):
        """Restore recently deleted files."""

        for recentlyDeleted in self.buffer_list: 
            self.fileList[recentlyDeleted[FILE_NAME]] = recentlyDeleted
        self.Render()
        self.und.Disable()

class FileDrop(wx.FileDropTarget):
    """Implement drag-and-drop functionality."""

    def __init__(self, window, parent):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.parent = parent

    def OnDropFiles(self, x, y, filenames):
        """If possible, drop selected files into main window."""

        try: 
           for file in filenames: 
              mypath = os.path.basename(file)
              self.parent.AddToList(file)
           self.parent.Render()
        except IOError, error:
           dlg = wx.MessageDialog(None, 'Error opening file\n' + str(error))
           dlg.ShowModal()

class HTMLWindow(wx.html.HtmlWindow):
    """Support the creation of a dialog box with html links."""

    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
   
    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())            

class ToolInfoDialog(wx.Dialog):
    """Display information about NLT."""

    def __init__(self, parent):
        wx.Dialog.__init__(self, None, title="NPR Loudness Tool", size=(250,300))
        hwin = HTMLWindow(self, -1, size=(400,200))
        infoText = """<p><b> NPR Loudness Tool</b><p>
The NPR(R) Loudness Tool (NLT) checks the levels of an audio file or files and indicates if they meet Public Radio Satellite System(R) (PRSS(R)) submission standards (http://prss.org/loudness). The NLT provides the option to adjust levels such that the resulting file is within the PRSS specifications.  Specifically, it adjusts the Integrated Loudness and the True Peaks, then saves the adjusted file.  You can install the NLT on your Mac or PC to check the levels of your audio files.
"""
        hwin.SetPage(infoText)
        btn = hwin.FindWindowById(wx.ID_OK)
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
        hwin.Show()

class InfoDialog(wx.Dialog):
    """Display information about NLT."""

    def __init__(self, parent):
        wx.Dialog.__init__(self, None, title="NPR Loudness Tool", size=(250,300))
        hwin = HTMLWindow(self, -1, size=(400,200))
        infoText = """<p><b> NPR Loudness Tool</b><p>
The NPR(R) Loudness Tool (NLT) checks the levels of an audio file or files and indicates if they meet Public Radio Satellite System(R) (PRSS(R)) submission standards (http://prss.org/loudness). The NLT provides the option to adjust levels such that the resulting file is within the PRSS specifications.  Specifically, it adjusts the Integrated Loudness and the True Peaks, then saves the adjusted file.  You can install the NLT on your Mac or PC to check the levels of your audio files.
"""
        hwin.SetPage(infoText)
        btn = hwin.FindWindowById(wx.ID_OK)
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
        hwin.Show()

class LicInfoDialog(wx.Dialog):
    """Display information about License."""

    def __init__(self, parent):
        wx.Dialog.__init__(self, None, title="License", size=(250,300))
        hwin = HTMLWindow(self, -1, size=(400,200))
        infoText = """<p><b> License</b><p>
NPR Loudness Tool (to check and adjust the loudness levels of audio files)<p>
Copyright (C) 2016 NPR <p>
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.  In addition, the names of NPR, NPR Labs, and the PRSS may not be used for publicity purposes to endorse or promote products based on this program without express prior written permission.
<p>
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
<p>
You should have received a copy of the GNU General Public License along with this program.  If not, see http://www.gnu.org/licenses/gpl-3.0.en.html. 
<p>
Source code for the NPR Loudness Tool is available at https://github.com/NPRLabs/Loudness.
<p>
FFmpeg library<p>
Copyright (C) 2012 Clement Boesch<p>
The NPR Loudness Tool uses the f_ebur128.c library, which is code of FFmpeg, https://www.ffmpeg.org/, licensed under the GPL 3 or later, http://www.gnu.org/licenses/gpl-3.0.en.html, and its source can be downloaded here:  https://ffmpeg.org/doxygen/2.8/f__ebur128_8c_source.html.   NPR does not own this code.  
<p>
"""
        hwin.SetPage(infoText)
        btn = hwin.FindWindowById(wx.ID_OK)
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
        hwin.Show()

class StandInfoDialog(wx.Dialog):
    """Display information about Loudness Standards."""

    def __init__(self, parent):
        wx.Dialog.__init__(self, None, title="Loudness Standards", size=(250,300))
        hwin = HTMLWindow(self, -1, size=(400,200))
        infoText = """<p><b> Loudness Standards</b><p>
The PRSS Audio Loudness Standard has been set at -24 Loudness Units Relative to Full Scale (LUFS), +/- 2 Loudness Units (LU), audio peaks less than or equal to -3 dBFS for sample peaks or less than or equal to -2 dBTP for True Peaks, meaning producers should strive to set their programs' audio levels at -24 LUFS, with a deviation range of +/- 2 LU and an audio peak at or below -3 dBFS or -2 dBTP.  See http://prss.org/loudness.  """
        hwin.SetPage(infoText)
        btn = hwin.FindWindowById(wx.ID_OK)
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
        hwin.Show()

class LabsInfoDialog(wx.Dialog):
    """Display information about NPR Labs."""

    def __init__(self, parent):
        wx.Dialog.__init__(self, None, title="NPR Labs", size=(250,300))
        hwin = HTMLWindow(self, -1, size=(400,200))
        infoText = """<p><b> NPR Labs</b><p>
NPR Labs is the nation's only not-for-profit broadcast technology research and development center.
"""
        hwin.SetPage(infoText)
        btn = hwin.FindWindowById(wx.ID_OK)
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
        hwin.Show()

class HelpInfoDialog(wx.Dialog):
    """Display information about Help."""

    def __init__(self, parent):
        wx.Dialog.__init__(self, None, title="Help", size=(250,300))
        hwin = HTMLWindow(self, -1, size=(400,200))
        infoText = """<p><b> Help</b><p>
You may contact NPR about this program at prsshelp@npr.org, or at 800.971.7677.  """
        hwin.SetPage(infoText)
        btn = hwin.FindWindowById(wx.ID_OK)
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
        hwin.Show()

class GPLInfoDialog(wx.Dialog):
    """Display information about GNU GENERAL PUBLIC LICENSE."""

    def __init__(self, parent):
        wx.Dialog.__init__(self, None, title="GNU GENERAL PUBLIC LICENSE", size=(250,300))
        hwin = HTMLWindow(self, -1, size=(400,200))
        infoText = """<p><b> GNU GENERAL PUBLIC LICENSE</b><p>
Version 3, 29 June 2007
<p>
Copyright (C) 2007 Free Software Foundation, Inc. <a href = http://fsf.org/>http://fsf.org/</a>
<p>
Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
<p>
Preamble
<p>
The GNU General Public License is a free, copyleft license for software and other kinds of works.
<p>
The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.
<p>
When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things.
<p>
To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.
<p>
For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.
<p>
Developers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal permission to copy, distribute and/or modify it.
<p>
For the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software. For both users' and authors' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions.
<p>
Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users' freedom to change the software. The systematic pattern of such abuse occurs in the area of products for individuals to use, which is precisely where it is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users.
<p>
Finally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free.
<p>
The precise terms and conditions for copying, distribution and modification follow.
<p>
TERMS AND CONDITIONS
<p>
0. Definitions.
<p>
"This License" refers to version 3 of the GNU General Public License.
<p>
"Copyright" also means copyright-like laws that apply to other kinds of works, such as semiconductor masks.
<p>
"The Program" refers to any copyrightable work licensed under this License. Each licensee is addressed as "you". "Licensees" and "recipients" may be individuals or organizations.
<p>
To "modify" a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy. The resulting work is called a "modified version" of the earlier work or a work "based on" the earlier work.
<p>
A "covered work" means either the unmodified Program or a work based on the Program.
<p>
To "propagate" a work means to do anything with it that, without permission, would make you directly or secondarily liable for infringement under applicable copyright law, except executing it on a computer or modifying a private copy. Propagation includes copying, distribution (with or without modification), making available to the public, and in some countries other activities as well.
<p>
To "convey" a work means any kind of propagation that enables other parties to make or receive copies. Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying.
<p>
An interactive user interface displays "Appropriate Legal Notices" to the extent that it includes a convenient and prominently visible feature that (1) displays an appropriate copyright notice, and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided), that licensees may convey the work under this License, and how to view a copy of this License. If the interface presents a list of user commands or options, such as a menu, a prominent item in the list meets this criterion.
<p>
1. Source Code.
<p>
The "source code" for a work means the preferred form of the work for making modifications to it. "Object code" means any non-source form of a work.
<p>
A "Standard Interface" means an interface that either is an official standard defined by a recognized standards body, or, in the case of interfaces specified for a particular programming language, one that is widely used among developers working in that language.
<p>
The "System Libraries" of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component, but which is not part of that Major Component, and (b) serves only to enable use of the work with that Major Component, or to implement a Standard Interface for which an implementation is available to the public in source code form. A "Major Component", in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs, or a compiler used to produce the work, or an object code interpreter used to run it.
<p>
The "Corresponding Source" for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work's System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work. For example, Corresponding Source includes interface definition files associated with source files for the work, and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work.
<p>
The Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source.
<p>
The Corresponding Source for a work in source code form is that same work.
<p>
2. Basic Permissions.
<p>
All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program. The output from running a covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law.
<p>
You may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force. You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works, provided that you comply with the terms of this License in conveying all material for which you do not control copyright. Those thus making or running the covered works for you must do so exclusively on your behalf, under your direction and control, on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you.
<p>
Conveying under any other circumstances is permitted solely under the conditions stated below. Sublicensing is not allowed; section 10 makes it unnecessary.
<p>
3. Protecting Users' Legal Rights From Anti-Circumvention Law.
<p>
No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996, or similar laws prohibiting or restricting circumvention of such measures.
<p>
When you convey a covered work, you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work, and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work's users, your or third parties' legal rights to forbid circumvention of technological measures.
<p>
4. Conveying Verbatim Copies.
<p>
You may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.
<p>
You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee.
<p>
5. Conveying Modified Source Versions.
<p>
You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:
<p>
    a) The work must carry prominent notices stating that you modified it, and giving a relevant date.
<p>
    b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to "keep intact all notices".
<p>
    c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permission if you have separately received it.
<p>
    d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so.
<p>
A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an "aggregate" if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate.
<p>
6. Conveying Non-Source Forms.
<p>
You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways:
<p>
    a) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange.
<p>
    b) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by a written offer, valid for at least three years and valid for as long as you offer spare parts or customer support for that product model, to give anyone who possesses the object code either (1) a copy of the Corresponding Source for all the software in the product that is covered by this License, on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or (2) access to copy the Corresponding Source from a network server at no charge.
<p>
    c) Convey individual copies of the object code with a copy of the written offer to provide the Corresponding Source. This alternative is allowed only occasionally and noncommercially, and only if you received the object code with such an offer, in accord with subsection 6b.
<p>
    d) Convey the object code by offering access from a designated place (gratis or for a charge), and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge. You need not require recipients to copy the Corresponding Source along with the object code. If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party) that supports equivalent copying facilities, provided you maintain clear directions next to the object code saying where to find the Corresponding Source. Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available for as long as needed to satisfy these requirements.
<p>
    e) Convey the object code using peer-to-peer transmission, provided you inform other peers where the object code and Corresponding Source of the work are being offered to the general public at no charge under subsection 6d.
<p>
A separable portion of the object code, whose source code is excluded from the Corresponding Source as a System Library, need not be included in conveying the object code work.
<p>
A "User Product" is either (1) a "consumer product", which means any tangible personal property which is normally used for personal, family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling. In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage. For a particular product received by a particular user, "normally used" refers to a typical or common use of that class of product, regardless of the status of the particular user or of the way in which the particular user actually uses, or expects or is expected to use, the product. A product is a consumer product regardless of whether the product has substantial commercial, industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product.
<p>
"Installation Information" for a User Product means any methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source. The information must suffice to ensure that the continued functioning of the modified object code is in no case prevented or interfered with solely because modification has been made.
<p>
If you convey an object code work under this section in, or with, or specifically for use in, a User Product, and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term (regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information. But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product (for example, the work has been installed in ROM).
<p>
The requirement to provide Installation Information does not include a requirement to continue to provide support service, warranty, or updates for a work that has been modified or installed by the recipient, or for the User Product in which it has been modified or installed. Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network.
<p>
Corresponding Source conveyed, and Installation Information provided, in accord with this section must be in a format that is publicly documented (and with an implementation available to the public in source code form), and must require no special password or key for unpacking, reading or copying.
<p>
7. Additional Terms.
<p>
"Additional permissions" are terms that supplement the terms of this License by making exceptions from one or more of its conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately under those permissions, but the entire Program remains governed by this License without regard to the additional permissions.
<p>
When you convey a copy of a covered work, you may at your option remove any additional permissions from that copy, or from any part of it. (Additional permissions may be written to require their own removal in certain cases when you modify the work.) You may place additional permissions on material, added by you to a covered work, for which you have or can give appropriate copyright permission.
<p>
Notwithstanding any other provision of this License, for material you add to a covered work, you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:
<p>
    a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or
<p>
    b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or
<p>
    c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or
<p>
    d) Limiting the use for publicity purposes of names of licensors or authors of the material; or
<p>
    e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or
<p>
    f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material (or modified versions of it) with contractual assumptions of liability to the recipient, for any liability that these contractual assumptions directly impose on those licensors and authors.
<p>
All other non-permissive additional terms are considered "further restrictions" within the meaning of section 10. If the Program as you received it, or any part of it, contains a notice stating that it is governed by this License along with a term that is a further restriction, you may remove that term. If a license document contains a further restriction but permits relicensing or conveying under this License, you may add to a covered work material governed by the terms of that license document, provided that the further restriction does not survive such relicensing or conveying.
<p>
If you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms.
<p>
Additional terms, permissive or non-permissive, may be stated in the form of a separately written license, or stated as exceptions; the above requirements apply either way.
<p>
8. Termination.
<p>
You may not propagate or modify a covered work except as expressly provided under this License. Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License (including any patent licenses granted under the third paragraph of section 11).
<p>
However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation.
<p>
Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice.
<p>
Termination of your rights under this section does not terminate the licenses of parties who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, you do not qualify to receive new licenses for the same material under section 10.
<p>
9. Acceptance Not Required for Having Copies.
<p>
You are not required to accept this License in order to receive or run a copy of the Program. Ancillary propagation of a covered work occurring solely as a consequence of using peer-to-peer transmission to receive a copy likewise does not require acceptance. However, nothing other than this License grants you permission to propagate or modify any covered work. These actions infringe copyright if you do not accept this License. Therefore, by modifying or propagating a covered work, you indicate your acceptance of this License to do so.
<p>
10. Automatic Licensing of Downstream Recipients.
<p>
Each time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that work, subject to this License. You are not responsible for enforcing compliance by third parties with this License.
<p>
An "entity transaction" is a transaction transferring control of an organization, or substantially all assets of one, or subdividing an organization, or merging organizations. If propagation of a covered work results from an entity transaction, each party to that transaction who receives a copy of the work also receives whatever licenses to the work the party's predecessor in interest had or could give under the previous paragraph, plus a right to possession of the Corresponding Source of the work from the predecessor in interest, if the predecessor has it or can get it with reasonable efforts.
<p>
You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License, and you may not initiate litigation (including a cross-claim or counterclaim in a lawsuit) alleging that any patent claim is infringed by making, using, selling, offering for sale, or importing the Program or any portion of it.
<p>
11. Patents.
<p>
A "contributor" is a copyright holder who authorizes use under this License of the Program or a work on which the Program is based. The work thus licensed is called the contributor's "contributor version".
<p>
A contributor's "essential patent claims" are all patent claims owned or controlled by the contributor, whether already acquired or hereafter acquired, that would be infringed by some manner, permitted by this License, of making, using, or selling its contributor version, but do not include claims that would be infringed only as a consequence of further modification of the contributor version. For purposes of this definition, "control" includes the right to grant patent sublicenses in a manner consistent with the requirements of this License.
<p>
Each contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor's essential patent claims, to make, use, sell, offer for sale, import and otherwise run, modify and propagate the contents of its contributor version.
<p>
In the following three paragraphs, a "patent license" is any express agreement or commitment, however denominated, not to enforce a patent (such as an express permission to practice a patent or covenant not to sue for patent infringement). To "grant" such a patent license to a party means to make such an agreement or commitment not to enforce a patent against the party.
<p>
If you convey a covered work, knowingly relying on a patent license, and the Corresponding Source of the work is not available for anyone to copy, free of charge and under the terms of this License, through a publicly available network server or other readily accessible means, then you must either (1) cause the Corresponding Source to be so available, or (2) arrange to deprive yourself of the benefit of the patent license for this particular work, or (3) arrange, in a manner consistent with the requirements of this License, to extend the patent license to downstream recipients. "Knowingly relying" means you have actual knowledge that, but for the patent license, your conveying the covered work in a country, or your recipient's use of the covered work in a country, would infringe one or more identifiable patents in that country that you have reason to believe are valid.
<p>
If, pursuant to or in connection with a single transaction or arrangement, you convey, or propagate by procuring conveyance of, a covered work, and grant a patent license to some of the parties receiving the covered work authorizing them to use, propagate, modify or convey a specific copy of the covered work, then the patent license you grant is automatically extended to all recipients of the covered work and works based on it.
<p>
A patent license is "discriminatory" if it does not include within the scope of its coverage, prohibits the exercise of, or is conditioned on the non-exercise of one or more of the rights that are specifically granted under this License. You may not convey a covered work if you are a party to an arrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work, and under which the third party grants, to any of the parties who would receive the covered work from you, a discriminatory patent license (a) in connection with copies of the covered work conveyed by you (or copies made from those copies), or (b) primarily for and in connection with specific products or compilations that contain the covered work, unless you entered into that arrangement, or that patent license was granted, prior to 28 March 2007.
<p>
Nothing in this License shall be construed as excluding or limiting any implied license or other defenses to infringement that may otherwise be available to you under applicable patent law.
<p>
12. No Surrender of Others' Freedom.
<p>
If conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot convey a covered work so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not convey it at all. For example, if you agree to terms that obligate you to collect a royalty for further conveying from those to whom you convey the Program, the only way you could satisfy both those terms and this License would be to refrain entirely from conveying the Program.
<p>
13. Use with the GNU Affero General Public License.
<p>
Notwithstanding any other provision of this License, you have permission to link or combine any covered work with a work licensed under version 3 of the GNU Affero General Public License into a single combined work, and to convey the resulting work. The terms of this License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such.
<p>
14. Revised Versions of this License.
<p>
The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.
<p>
Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License "or any later version" applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation.
<p>
If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program.
<p>
Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version.
<p>
15. Disclaimer of Warranty.
<p>
THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
<p>
16. Limitation of Liability.
<p>
IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
<p>
17. Interpretation of Sections 15 and 16.
<p>
If the disclaimer of warranty and limitation of liability provided above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee.
<p>
END OF TERMS AND CONDITIONS
<p>
How to Apply These Terms to Your New Programs
<p>
If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms.
<p>
To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found.
<p>
 <one line to give the program's name and a brief idea of what it does.>
<p>
Copyright (C) <year>  <name of author>
<p>
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by  the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
<p>
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
<p>

You should have received a copy of the GNU General Public License along with this program.  If not, see <a href = http://www.gnu.org/licenses/>www.gnu.org/licenses</a>.
<p>
Also add information on how to contact you by electronic and paper mail.
<p>
If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:
<p>
<program>  Copyright (C) <year>  <name of author>
<p>
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
<p>
This is free software, and you are welcome to redistribute it under certain conditions; type `show c' for details.
<p>
The hypothetical commands `show w' and `show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box".
<p>
You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <a href = http://www.gnu.org/licenses/>www.gnu.org/licenses</a>.
<p>
The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with the library. If this is what you want to do, use the GNU Lesser General Public License instead of this License. But first, please read <a href = http://www.gnu.org/philosophy/why-not-lgpl.html>www.gnu.org/philosophy/why-not-lgpl.html</a>.
<p>

<p>

<p>

"""
        hwin.SetPage(infoText)
        btn = hwin.FindWindowById(wx.ID_OK)
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
        hwin.Show()

    def OnSameFold(self, event):
        self.adjFileLoc.Disable()

    def OnDiffFold(self, event):
        self.adjFileLoc.Enable()

    def OnLogFileLoc(self, event):
        self.parent.logFileLoc = self.logFileLoc.GetTextCtrlValue()

    def OnAdjFileLoc(self, event):
        self.parent.adjFileLoc = self.adjFileLoc.GetTextCtrlValue()

    def OnOverwrite(self, event):
        self.parent.overwrite = self.overwrite.GetValue() 

    def OnIntLoudSpin(self, event):
        self.parent.targetIL = self.intloudSpin.GetValue() 

    def OnPeakSpin(self, event):
        self.parent.targetPeak = self.peakSpin.GetValue() 

    def OnGraceSpin(self, event):
        self.parent.grace = self.graceSpin.GetValue() 

    def OnRestoreDefaults(self, event):
        """Restore default settings (for current session)."""

        self.parent.targetPeak = TARGET_PEAK_DEFAULT
        self.peakSpin.SetValue(TARGET_PEAK_DEFAULT)

        self.parent.targetIL = TARGET_IL_DEFAULT
        self.intloudSpin.SetValue(TARGET_IL_DEFAULT)

        self.parent.grace = GRACE_DEFAULT
        self.graceSpin.SetValue(GRACE_DEFAULT)

        self.parent.overwrite = OVERWRITE_DEFAULT
        self.overwrite.SetValue(OVERWRITE_DEFAULT)

        self.parent.sameFold = SAME_FOLDER_DEFAULT
        self.sameFold.SetValue(SAME_FOLDER_DEFAULT)   

        self.parent.logFileLoc = LOG_FILE_LOC_DEFAULT
        self.logFileLoc.SetPath(LOG_FILE_LOC_DEFAULT)

        self.parent.adjFileLoc = ADJ_FILE_LOC_DEFAULT
        self.adjFileLoc.SetPath(ADJ_FILE_LOC_DEFAULT)

    def OnSaveSettings(self, event):
        """Write current preferences to the config file for later retrieval."""

        self.parent.config['TARGET_IL'] = str(self.intloudSpin.GetValue())
        self.parent.config['TARGET_PEAK'] = str(self.peakSpin.GetValue())
        self.parent.config['GRACE'] = str(self.graceSpin.GetValue())
        self.parent.config['OVERWRITE'] = self.overwrite.GetValue()
        self.parent.config['SAME_FOLDER'] = self.sameFold.GetValue()
        self.parent.config['DIFF_FOLDER'] = self.diffFold.GetValue()
        self.parent.config['ADJ_FILE_LOC'] = str(self.adjFileLoc.GetTextCtrlValue())
        self.parent.config['LOG_FILE_LOC'] = str(self.logFileLoc.GetTextCtrlValue())

        self.parent.WriteConfig()

        dlg = wx.MessageDialog(self, "Settings saved to configuration file.", "Settings saved.", style=wx.OK|wx.CENTRE)
        dlg.ShowModal()
        dlg.Destroy()

    def OnClose(self, event): 
        """Preferences menu closes without settings being changed."""

        self.Close()

    def OnApply(self, event):
        """Apply user preferences to the current session."""

        self.parent.targetPeak = self.peakSpin.GetValue()  
        self.parent.targetIL = self.intloudSpin.GetValue()
        self.parent.grace = self.graceSpin.GetValue()
        self.parent.overwrite = self.overwrite.GetValue()
        self.parent.sameFold = self.sameFold.GetValue()
        self.parent.adjFileLoc = self.adjFileLoc.GetTextCtrlValue()
        self.parent.logFileLoc = self.logFileLoc.GetTextCtrlValue()
 
        self.Close()

def str2bool(v):
   """Convert the string 'True' to its boolean equivalent."""
   return v in ("True")

# Build the application

MainWindow(None, -1, 'NPR Loudness Tool')
app.MainLoop()