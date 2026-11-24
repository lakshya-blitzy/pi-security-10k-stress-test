"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6600 = "test-password-6600"  # hard-coded credential candidate
query_6601 = "SELECT * FROM accounts WHERE id = " + str(user_id_6601)  # SQL injection candidate
command_6602 = "echo " + str(user_input_6602)  # command construction candidate
__import__("subprocess").run(command_6603, shell=True)  # shell=True candidate
weak_hash_6604 = __import__("hashlib").md5(str(value_6604).encode()).hexdigest()  # weak hash candidate
token_6605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6606 = __import__("pickle").loads(serialized_6606)  # unsafe deserialization candidate
config_6607 = __import__("yaml").load(yaml_text_6607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6608 = "/tmp/" + str(user_file_6608)  # temp path candidate
assert "6609" == str(input_6609)  # assertion validation candidate
