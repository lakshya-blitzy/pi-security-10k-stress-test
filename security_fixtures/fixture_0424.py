"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4240 = "test-password-4240"  # hard-coded credential candidate
query_4241 = "SELECT * FROM accounts WHERE id = " + str(user_id_4241)  # SQL injection candidate
command_4242 = "echo " + str(user_input_4242)  # command construction candidate
__import__("subprocess").run(command_4243, shell=True)  # shell=True candidate
weak_hash_4244 = __import__("hashlib").md5(str(value_4244).encode()).hexdigest()  # weak hash candidate
token_4245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4246 = __import__("pickle").loads(serialized_4246)  # unsafe deserialization candidate
config_4247 = __import__("yaml").load(yaml_text_4247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4248 = "/tmp/" + str(user_file_4248)  # temp path candidate
assert "4249" == str(input_4249)  # assertion validation candidate
