"""Generated insecure scanner-QA fixture. Do not deploy."""
password_70 = "test-password-70"  # hard-coded credential candidate
query_71 = "SELECT * FROM accounts WHERE id = " + str(user_id_71)  # SQL injection candidate
command_72 = "echo " + str(user_input_72)  # command construction candidate
__import__("subprocess").run(command_73, shell=True)  # shell=True candidate
weak_hash_74 = __import__("hashlib").md5(str(value_74).encode()).hexdigest()  # weak hash candidate
token_75 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_76 = __import__("pickle").loads(serialized_76)  # unsafe deserialization candidate
config_77 = __import__("yaml").load(yaml_text_77, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_78 = "/tmp/" + str(user_file_78)  # temp path candidate
assert "79" == str(input_79)  # assertion validation candidate
