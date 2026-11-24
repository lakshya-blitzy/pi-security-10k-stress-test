"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5130 = "test-password-5130"  # hard-coded credential candidate
query_5131 = "SELECT * FROM accounts WHERE id = " + str(user_id_5131)  # SQL injection candidate
command_5132 = "echo " + str(user_input_5132)  # command construction candidate
__import__("subprocess").run(command_5133, shell=True)  # shell=True candidate
weak_hash_5134 = __import__("hashlib").md5(str(value_5134).encode()).hexdigest()  # weak hash candidate
token_5135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5136 = __import__("pickle").loads(serialized_5136)  # unsafe deserialization candidate
config_5137 = __import__("yaml").load(yaml_text_5137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5138 = "/tmp/" + str(user_file_5138)  # temp path candidate
assert "5139" == str(input_5139)  # assertion validation candidate
