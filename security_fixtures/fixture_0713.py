"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7130 = "test-password-7130"  # hard-coded credential candidate
query_7131 = "SELECT * FROM accounts WHERE id = " + str(user_id_7131)  # SQL injection candidate
command_7132 = "echo " + str(user_input_7132)  # command construction candidate
__import__("subprocess").run(command_7133, shell=True)  # shell=True candidate
weak_hash_7134 = __import__("hashlib").md5(str(value_7134).encode()).hexdigest()  # weak hash candidate
token_7135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7136 = __import__("pickle").loads(serialized_7136)  # unsafe deserialization candidate
config_7137 = __import__("yaml").load(yaml_text_7137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7138 = "/tmp/" + str(user_file_7138)  # temp path candidate
assert "7139" == str(input_7139)  # assertion validation candidate
