from django.shortcuts import render
from io import BytesIO
import time
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from reportlab.lib.units import inch

from reportlab.platypus.tables import Table,TableStyle,colors
#from my_table_data import my_data # import the data
# my_path='G:\\My drive\\testing\\pypdf2\\my_pdf.pdf' # change path, file name 

# my_data= [['ID', 'Name', 'Class', 'Mark', 'Gender'],
# (1, 'John Deo', 'Four', 75, 'female'),
# (2, 'Max Ruin', 'Three', 85, 'male'),
# (3, 'Arnold', 'Three', 55, 'male')]

# my_doc=SimpleDocTemplate(my_path,pagesize=letter)
# c_width=[0.4*inch,1.5*inch,1*inch,1*inch,1*inch]
# t=Table(my_data,rowHeights=20,repeatRows=1,colWidths=c_width)
# t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightgreen),
# ('FONTSIZE',(0,0),(-1,-1),10)]))
# elements=[]
# elements.append(t)
# my_doc.build(elements) 

def gen_table(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="table.pdf"'
    doc = SimpleDocTemplate(response,pagesize=letter, rightMargin=72,leftMargin=72, topMargin=72,bottomMargin=18)
    
    my_data= [['ID', 'Name', 'Class', 'Mark', 'Gender'],
    (1, 'John Deo', 'Four', 75, 'female'),
    (2, 'Max Ruin', 'Three', 85, 'male'),
    (3, 'Arnold', 'Three', 55, 'male')]

    c_width=[0.4*inch,1.5*inch,1*inch,1*inch,1*inch]
    t=Table(my_data,rowHeights=20,repeatRows=1,colWidths=c_width)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightgreen),
    ('FONTSIZE',(0,0),(-1,-1),10)]))
    elements=[]
    elements.append(t)

    doc.build(elements)
    return response

def home(request):
    return render(request, 'app/home.html')


def generate_helloWorld(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hello.pdf"'
    p = canvas.Canvas(response)
    p.drawString(30, 750, "Hello World!")
    p.showPage()
    p.save()

    return response


def generate_form(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="form.pdf"'
    p = canvas.Canvas(response)
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)
    p.drawString(30,750,'OFFICIAL COMMUNIQUE')
    p.drawString(30,735,'OF XYZ INDUSTRIES')
    p.drawString(500,750,"12/12/2010")
    p.line(480,747,580,747)
    p.drawString(275,725,'AMOUNT OWED:')
    p.drawString(500,725,"BDT 5000.00")
    p.line(378,723,580,723)
    p.drawString(30,703,'RECEIVED BY:')
    p.line(120,700,580,700)
    p.drawString(120,703,"Ms. Z")

    p.showPage()
    p.save()

    return response



def generate_letter(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="letter.pdf"'

    doc = SimpleDocTemplate(response,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    Story=[]
    logo = "static/pylogo.jpg"
    magName = "TOTO"
    issueNum = 12
    subPrice = "99.00"
    limitedDate = "03/05/2023"
    freeGift = "tin foil hat"

    formatted_time = time.ctime()
    full_name = "chottola chotto"
    address_parts = ["chotto St.", "chotto town, chottogram"]

    im = Image(logo, 1*inch, 1*inch)
    Story.append(im)

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '%s' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '%s' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))       
    for part in address_parts:
        ptext = '%s' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   

    Story.append(Spacer(1, 12))
    ptext = 'Dear %s:' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = """accusamus dolores quos eius rerum iure fuga voluptate aperiam quo quod voluptates culpa ducimus? Ex, doloremque asperiores voluptatibus laborum odio veniam quam quibusdam. Ducimus minima omnis mollitia enim, a voluptatum repellendus adipisci esse similique neque, doloribus corporis aperiam autem rerum beatae repudiandae unde reiciendis fuga accusantium accusamus numquam obcaecati ipsam non, iste maiores! Quisquam accusamus molestiae accusantium optio neque numquam eum quam quasi, nulla, voluptatem nam exercitationem sunt labore eligendi. Labore impedit ducimus itaque dolores quam explicabo laboriosam porro pariatur numquam ratione quia, ipsa, incidunt magnam, veniam illum necessitatibus eius dolore debitis. Sequi debitis culpa minima et veritatis reprehenderit cum. At exercitationem enim accusamus nam, ab ipsum repellat eligendi. Est amet suscipit expedita deserunt nostrum. Animi adipisci tempora, ea autem ipsa qui recusandae quibusdam deleniti aliquam, in asperiores aspernatur atque architecto facere temporibus nihil, minus repellat laboriosam. Dolorem facilis officiis quae, quos illum distinctio, cupiditate itaque amet eaque perspiciatis repellendus aspernatur minima repudiandae. Minima minus eveniet iusto non assumenda natus animi quibusdam porro consectetur asperiores sequi aspernatur repellendus enim soluta suscipit, vel blanditiis cumque dolores similique delectus eligendi odio, tenetur aliquid? Laborum consequatur quibusdam ipsam, ipsum qui ea voluptas consectetur iste facilis, rerum doloremque nisi perferendis excepturi enim quidem cumque odio temporibus totam assumenda. In quasi, voluptatibus quis possimus ea vitae ipsa? Velit nobis provident laboriosam perferendis vel labore quia rerum accusantium dignissimos. Praesentium ullam ipsa corrupti vel optio dignissimos reprehenderit vitae reiciendis, quia tenetur harum officia veniam recusandae dolorum, nesciunt excepturi natus laudantium eveniet dolorem ad inventore quod ex temporibus minus? Nesciunt ducimus, exercitationem quae doloribus omnis tempora expedita harum esse recusandae. Hic nihil voluptatum deleniti molestiae adipisci eius earum ad! Soluta nam repudiandae nostrum, tempora, reprehenderit doloremque est quae et, aut cum quidem dolorem saepe dolores nobis sit fuga velit iure voluptas sunt provident repellendus aperiam tempore id? Tempora dignissimos a, voluptas tenetur quibusdam blanditiis inventore asperiores. Vitae assumenda possimus iusto asperiores eaque porro neque architecto, eum voluptatem blanditiis? Esse voluptas quod, maiores fugiat at ducimus tempore ipsa laboriosam iste, quos qui soluta! Unde doloribus nihil in ut exercitationem libero, sequi maiores atque nam, eius aspernatur consectetur enim. Minima velit vel delectus veritatis quidem beatae autem eum, accusamus sed id inventore laudantium sequi asperiores quae. Enim maiores voluptates, quisquam animi tenetur quia incidunt neque aut? Vero consequatur suscipit natus autem dignissimos earum deleniti porro, nesciunt sequi delectus officia, animi facere, praesentium id nostrum quia blanditiis excepturi. Non ipsam accusamus maiores, fuga animi ratione voluptas quod, assumenda temporibus excepturi incidunt dicta. Facilis non in fuga aliquam incidunt, voluptatibus neque ut harum laudantium voluptate temporibus deleniti praesentium recusandae eius nulla, corrupti consequatur ex tempore esse ipsum optio suscipit, perferendis eligendi? Quis quidem animi libero perspiciatis nesciunt, adipisci recusandae esse hic, eos et quibusdam cupiditate harum nostrum, consectetur porro asperiores laborum perferendis. Velit sunt voluptatem voluptates in tenetur soluta vel, omnis qui odio. Perspiciatis velit illum veniam necessitatibus quisquam, deserunt aperiam aut, corrupti facilis ratione nihil hic ipsam eius minima ullam a magnam vitae fugit. Delectus id porro ad error illum debitis, quos ratione tempore aliquam, aspernatur ipsa nesciunt molestias fugit assumenda! Sint quam nisi mollitia itaque, architecto aperiam dolorem tenetur sunt corrupti fugiat obcaecati totam molestias, quod voluptas blanditiis necessitatibus natus aliquam enim in dolorum minus magnam ex vel? Fugiat, incidunt. Inventore odit quibusdam distinctio rerum accusantium iusto ducimus cum molestias ad debitis. Unde neque exercitationem, ullam est nostrum illum reprehenderit necessitatibus doloremque aliquam nihil quasi labore consectetur odio corrupti, ut consequatur eaque assumenda autem maiores. Esse at, quos cupiditate est soluta sunt minus vitae molestiae! Est non modi consequuntur facilis eos? Odit recusandae aut veritatis quis ea rerum, quasi labore voluptates! Qui architecto, accusamus fugiat eaque voluptas vero repudiandae aperiam quod laborum dolore corrupti suscipit voluptatem molestias assumenda iusto, tempore quasi molestiae! Corrupti tempora fuga facilis deleniti ea! Suscipit quae numquam hic iure voluptatum laudantium repudiandae et ipsum dignissimos sint voluptatibus quas nihil facilis, quasi quo mollitia blanditiis a tempora culpa vero alias! Cum illo ut animi consequatur facere dicta repudiandae enim sint, asperiores veniam perspiciatis! Esse velit, odio facilis vel libero fugiat, ipsum quod soluta animi saepe ut molestias aliquam deserunt excepturi sit dolorem eum aperiam quia? Aspernatur at a porro sint dolor, iusto corrupti quis libero labore nostrum est autem minima id dolores culpa debitis eos facere optio iure adipisci ducimus voluptates vitae deserunt molestias. Iste deserunt accusamus dolores perspiciatis esse porro ea nesciunt vel dolore, illum doloremque perferendis? At consequatur cum, soluta ab voluptate blanditiis, dolores delectus fugit maxime sequi nisi. Cumque sunt corrupti fuga pariatur nostrum hic laudantium possimus explicabo vero, illo distinctio eaque quam adipisci laboriosam nihil voluptatum. Quasi, aut amet illo excepturi facilis repudiandae maiores voluptas officia assumenda minus, perferendis voluptatem dicta, ea vel eos quisquam delectus blanditiis. Tempore beatae, veniam cum, consequatur non accusamus minus recusandae praesentiureprehenderit. Facilis odit perspiciatis molestias illum, dignissimos alias, molestiae non cupiditate ipsa iste deleniti doloremque aspernatur repellat sapiente at provident suscipit quo repudiandae quisquam et unde? Inventore aliquid laudantium fugiat! Iste commodi provident hic cumque aliquid quaerat eaque adipisci nam repellat, ullam illum, aspernatur accusamus voluptatem! Corporis odio quibusdam ut, dolores culpa quaerat, nemo iure, eius dolorem nobis non! Doloremque fugiat voluptate soluta enim debitis consectetur aut. Fuga pariatur rem, eveniet quaerat atque fugiat voluptatibus, reiciendis recusandae sequi ex odio quasi possimus deleniti nemo at error. Aliquam ut odio aperiam maxime consequatur unde labore adipisci fugit saepe? Dignissimos molestiae modi accusamus ut quam exercitationem cum voluptatem voluptate? Sint voluptas distinctio laudantium ab est repellat excepturi, commodi voluptatibus placeat quas earum labore id porro quia! Nihil magni aliquam perferendis quia at nisi dolor soluta enim, quos iusto! Expedita deserunt maiores culpa commodi voluptate eos eum libero, quos, eius placeat minima inventore quas provident! Impedit voluptates numquam itaque omnis sint ut, recusandae explicabo facilis! Nulla numquam adipisci, dolor harum quas nesciunt delectus suscipit odio labore officia omnis saepe consectetur corrupti ut nemo laborum sunt voluptates rerum impedit magnam veritatis eos accusamus. Cumque ratione totam atque facilis repudiandae, fugiat dolor? Perferendis nesciunt magni fugiat consequuntur asperiores accusantium. Debitis ut in fugiat voluptatem veritatis voluptatum, blanditiis similique quaerat nam eaque impedit odio est corporis omnis id quos placeat obcaecati aut, alias incidunt! Nihil ipsa consequuntur iure sunt reprehenderit earum quibusdam dicta. Soluta dolor possimus cumque aliquid pariatur doloribus et? Error autem labore iusto qui ipsam harum, mollitia perspiciatis sequi cumque, praesentium inventore delectus illum reiciendis excepturi placeat sit amet voluptatibus fugiat! Maiores error alias sit recusandae cupiditate fuga commodi. Cumque qui quia natus rerum placeat repellat dignissimos unde commodi reprehenderit ea laudantium assumenda, illum, hic distinctio voluptate praesentium at ab ipsum reiciendis explicabo aliquam quos? Non nihil quam maiores ab nobis impedit alias? In laborum voluptates impedit aperiam eligendi cupiditate unde, saepe quia facilis inventore. Repellat, doloremque? Sit, inventore architecto hic tempore quod velit sunt modi earum, nesciunt quas eaque accusamus dolores. Dicta illo vel, eligendi ut, sint et pariatur aliquam eum quasi nulla veniam voluptas minus aut. Pariatur enim quam, dignissimos error amet dolorum sed nihil ducimus aperiam cupiditate, unde accusamus, explicabo voluptatibus sequi obcaecati ex incidunt ea culpa. Necessitatibus cumque recusandae, quam adipisci ut repudiandae quae at facere harum eius ea expedita? Placeat accusantium nisi odit magni et soluta minima commodi repellat, dignissimos rem modi veniam dolor omnis optio ut deserunt, sequi, minus mollitia doloribus ullam est eum? Dolores eum exercitationem aliquid ratione enim natus totam dolor, reiciendis quis possimus aperiam ab, laudantium veniam? Voluptate, ullam? Reprehenderit laudantium non eius ut maxime est, possimus dolorum dolore ad eum architecto! Ipsum veritatis cupiditate aspernatur iusto accusamus id delectus deserunt rerum aut. Eum ducimus nam adipisci voluptates explicabo minima vel aliquid consequatur ex distinctio magni perferendis corporis rerum, autem consectetur sunt et quam doloremque, provident recusandae praesentium iure aut? Quis aperiam temporibus perferendis quaerat! Neque, non delectus fugiat debitis numquam aut, unde quam quaerat natus autem qui ratione beatae voluptatibus quae illo? Nesciunt culpa aliquid obcaecati aspernatur soluta. Aspernatur error sed dignissimos obcaecati id, quasi accusamus odit? Vero laudanre quod nisi, perspiciatis similique doloremque repellat molestiae recusandae! Veniam ad aliquid enim labore nihil at impedit quas placeat amet voluptatibus, quasi nesciunt beatae cumque odit pariatur. Esse, architecto nemo rem omnis eum magni! Voluptas architecto earum officia doloribus dolor natus itaque quasi, facere accusantium eos ipsum. Provident modi rem incidunt possimus delectus? Voluptate libero quidem, harum perspiciatis minus voluptas dolorem veniam perferendis ab nobis, quasi accusamus molestias culpa, quas facilis odio? Saepe laboriosam esse amet, optio ratione natus aspernatur architecto qui eaque earum? Distinctio animi blanditiis quas molestias. Harum eveniet quia vel ipsum, quo pariatur. Eveniet numquam perspiciatis quo, quisquam, tenetur dolores cupiditate similique praesentium quae placeat totam iusto, impedit aspernatur doloremque adipisci alias natus repellat est. Voluptas quam consequuntur magni praesentium et temporibus tenetur numquam id molestias eveniet beatae labore modi ut obcaecati animi soluta, distinctio, tempore dolorum, nostrum deleniti cupiditate enim nam cumque optio. Excepturi, culpa laboriosam repudiandae molestiae cupiditate, voluptatum ipsum id veniam blanditiis nulla itaque voluptatibus aperiam quos in veritatis qui deserunt inventore dolore facere libero velit sapiente rem modi deleniti! Illo minima sapiente deleniti quam saepe ducimus molestias perspiciatis officiis, modi pariatur? Praesentium quidem eveniet provident, fugiat repellendus at commodi adipisci animi laboriosam ea consectetur quibusdam nesciunt alias vel, expedita nobis obcaecati aspernatur magnam architecto eaque! Cumque ducimus aliquam commodi quis odit eius, vel quas cum dolor corrupti deserunt. Soluta a veritatis aliquam at assumenda alias nemo minus? Temporibus illum similique aut itaque, molestias totam maxime ducimus ratione dolorem nemo exercitationem animi atque quaerat quas quisquam, officia aliquam possimus, dicta necessitatibus quam quo libero recusandae corporis. Quae aliquid iusto similique adipisci tempora necessitatibus soluta sapiente fugiat debitis quidem odit nisi dicta, eum eveniet pariatur corrupti quaerat voluptatum non voluptates enim? Velit, fugit officia eligendi, aliquid iusto sunt harum, dolor laudantium fugiat labore enim sapiente omnis. Corporis odit deleniti distinctio exercitationem eveniet. Reiciendis velit, eius accusamus maxime cum at facere quia repudiandae quo veritatis iure! Ducimus voluptas cum, inventore, ipsum voluptatibus nesciunt amet sint distinctio nihil est iure doloribus? Eum laborum aperiam explicabo ipsum rem soluta aspernatur officiis. Molestiae, corporis non. Similique assumenda dolor cum laboriosam asperiores ea excepturi, aperiam unde distinctio blanditiis sed, ratione, nihil maiores. Aliquid necessitatibus eligendi praesentium alias impedit velit laborum consequatur nostrum voluptatum cumque voluptates omnis facere aliquam a nesciunt neque voluptatibus saepe hic temporibus cum, minus soluta? A atque incidunt error repellat quasi quas molestiae nisi, quam sed tenetur amet eius laudantium corrupti impedit, maxime esse et cum ipsam. Maxime neque officiis eveniet, optio dolor aut quo delectus autem sequi id, asperiores a alias illum! Delectus alias laboriosam rerum iure eum voluptatibus voluptatem eaque, aliquid, accusamus dignissimos quibusdam qui animi quia, molestiae consectetur facilis labore dolorum! Fugiat ab accusantium doloremque quas. Veniam, in? Sequi velit in repellendus laboriosam quod aliquid, deleniti autem officia pariatur provident placeat magni labore voluptates iure explicabo ipsum error tempora aliquam, minima ab dicta sunt? Laudantium, incidunt tenetur eveniet ex non similique hic nulla accusantium cumque officiis et explicabo ab fugiat ipsa, impedit maxime! Fuga totam nesciunt dignissimos? Perspiciatis optio illum reprehenderit consectetur ullam voluptas laborum, amet temporibus esse. Ipsam tempora nam fugit. Beatae, accusamus. Voluptate nesciunt maiores et dolores exercitationem ullam aut sapiente explicabo architecto optio, tempore vero delectus illum eum? Nesciunt dicta, similique soluta magni maiores expedita consequuntur aliquid quae accusamus nulla fugiat molestiae! Qui quaerat id quia ut nemo est ipsa pariatur corporis impedit repellendus, deserunt at cum consequuntur facere voluptas nisi enim tempora consectetur maiores voluptates doloremque assumenda? Necessitatibus facere sed vero reiciendis quos dolorem, et est molestiae ratione, saepe alias facilis, iste aut pariatur quam debitis ex numquam. Veniam voluptatum distinctio architecto, aliquam impedit laudantium magni voluptas reprehenderit, unde facere, quaerat soluta nam ameluta debitis unde delectus in laboriosam molestiae nesciunt deleniti, consequuntur voluptates placeat libero earum consectetur excepturi iusto iste recusandae ipsa repellendus eius voluptatem accusamus hic provident, cupiditate rem? Ad commodi corporis atque iste voluptates quidem iure cumque dolorem eos architecto vitae voluptas est aspernatur enim cum, aperiam ducimus at rem sint modi suscipit porro. Quasi et excepturi voluptas earum officiis numquam provident recusandae amet, explicabo doloribus eaque repellendus sed porro impedit mollitia, ipsam pariatur, non consequatur officia reprehenderit. Ducimus vero eligendi amet dicta explicabo. Corporis dolore accusamus mollitia iste doloribus in ipsum assumenda blanditiis! Beatae eum quibusdam fugiat itaque voluptatem voluptatum architecto sit ipsam, eos quod, minima et quis aliquam magni quae tempora aliquid commodi! Explicabo doloremque reiciendis ipsa deleniti quibusdam provident corrupti Ipsum iste consequatur quam. Aliquid tenetur qui veniam molestiae et rerum? Ipsa iure dolorem eius. Reiciendis quisquam, tempore eos quam eum, excepturi sint rem omnis, saepe doloribus cumque modi incidunt distinctio maiores voluptatem assumenda fugiat corporis voluptas vel earum repellat a"""
    ptext += 'We would like to welcome you to our subscriber base for %s Magazine! \
            You will receive %s issues at the excellent introductory price of $%s. Please respond by\
            %s to start receiving your subscription and get the following free gift: %s.' % (magName,issueNum,subPrice, limitedDate,freeGift)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = 'Thank you very much and we look forward to serving you.'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = 'Sincerely,'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = 'Ms. Z'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)

    return response

