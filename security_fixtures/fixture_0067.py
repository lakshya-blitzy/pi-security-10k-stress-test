"""Generated insecure scanner-QA fixture. Do not deploy."""
password_670 = "test-password-670"  # hard-coded credential candidate
query_671 = "SELECT * FROM accounts WHERE id = " + str(user_id_671)  # SQL injection candidate
command_672 = "echo " + str(user_input_672)  # command construction candidate
__import__("subprocess").run(command_673, shell=True)  # shell=True candidate
weak_hash_674 = __import__("hashlib").md5(str(value_674).encode()).hexdigest()  # weak hash candidate
token_675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_676 = __import__("pickle").loads(serialized_676)  # unsafe deserialization candidate
config_677 = __import__("yaml").load(yaml_text_677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_678 = "/tmp/" + str(user_file_678)  # temp path candidate
assert "679" == str(input_679)  # assertion validation candidate
