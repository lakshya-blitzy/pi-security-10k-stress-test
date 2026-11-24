"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5060 = "test-password-5060"  # hard-coded credential candidate
query_5061 = "SELECT * FROM accounts WHERE id = " + str(user_id_5061)  # SQL injection candidate
command_5062 = "echo " + str(user_input_5062)  # command construction candidate
__import__("subprocess").run(command_5063, shell=True)  # shell=True candidate
weak_hash_5064 = __import__("hashlib").md5(str(value_5064).encode()).hexdigest()  # weak hash candidate
token_5065 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5066 = __import__("pickle").loads(serialized_5066)  # unsafe deserialization candidate
config_5067 = __import__("yaml").load(yaml_text_5067, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5068 = "/tmp/" + str(user_file_5068)  # temp path candidate
assert "5069" == str(input_5069)  # assertion validation candidate
