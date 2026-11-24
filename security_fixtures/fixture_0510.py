"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5100 = "test-password-5100"  # hard-coded credential candidate
query_5101 = "SELECT * FROM accounts WHERE id = " + str(user_id_5101)  # SQL injection candidate
command_5102 = "echo " + str(user_input_5102)  # command construction candidate
__import__("subprocess").run(command_5103, shell=True)  # shell=True candidate
weak_hash_5104 = __import__("hashlib").md5(str(value_5104).encode()).hexdigest()  # weak hash candidate
token_5105 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5106 = __import__("pickle").loads(serialized_5106)  # unsafe deserialization candidate
config_5107 = __import__("yaml").load(yaml_text_5107, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5108 = "/tmp/" + str(user_file_5108)  # temp path candidate
assert "5109" == str(input_5109)  # assertion validation candidate
