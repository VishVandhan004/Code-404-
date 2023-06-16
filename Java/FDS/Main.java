class Beauty
{
    String name;
    String SID;
    int cost;
    Beauty(String name,String SID,int cost)
    {
        this.name=name;
        this.SID=SID;
        this.cost=cost;
    }
    double sell()
    {
        double tot=(18/100)*cost+cost;
        return tot;
    }
}
class products
{
    String name;
    String ID;
    int cost;
    products(String name,String ID,int cost)
    {
        this.name=name;
        this.ID=ID;
        this.cost=cost;
    }
    double sell()
    {
        double total=(5/100)*cost+cost;
        return total;
    }
}
class Main
{
    public static void main(String[] args) 
    {
        Beauty b1=new Beauty("FacePack","A12",200);
        Beauty b2=new Beauty("Perfume","B12",300);
        Beauty b3=new Beauty("Powder","C12",400);
        products p1=new products("Atta","D12",100);
        products p2=new products("Sugar","E12",50);
        System.out.println("NAME"+"      "+"ID"+"    "+"COST");
        System.out.println(b1.name+"  "+b1.SID+"   "+b1.cost);
        System.out.println(b2.name+"   "+b2.SID+"   "+b2.cost);
        System.out.println(b3.name+"    "+b3.SID+"   "+b3.cost);
        System.out.println(p1.name+"      "+p1.ID+"   "+p1.cost);
        System.out.println(p2.name+"     "+p2.ID+"   "+p2.cost);
        b1.sell();
        b2.sell();
        b3.sell();
        p1.sell();
        p2.sell();
        double total=(b1.sell()+b2.sell()+b3.sell()+p1.sell()+p2.sell());
        System.out.println("Total bill before discount:"+total);
        double discount=(2.00/100.00)*total;
        double tot=total-discount;
        System.out.println("Total bill after discount:"+tot);
    }
}
