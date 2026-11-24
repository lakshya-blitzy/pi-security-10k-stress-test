"""Generated insecure scanner-QA fixture. Do not deploy."""
password_600 = "test-password-600"  # hard-coded credential candidate
query_601 = "SELECT * FROM accounts WHERE id = " + str(user_id_601)  # SQL injection candidate
command_602 = "echo " + str(user_input_602)  # command construction candidate
__import__("subprocess").run(command_603, shell=True)  # shell=True candidate
weak_hash_604 = __import__("hashlib").md5(str(value_604).encode()).hexdigest()  # weak hash candidate
token_605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_606 = __import__("pickle").loads(serialized_606)  # unsafe deserialization candidate
config_607 = __import__("yaml").load(yaml_text_607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_608 = "/tmp/" + str(user_file_608)  # temp path candidate
assert "609" == str(input_609)  # assertion validation candidate
