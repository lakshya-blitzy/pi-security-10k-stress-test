"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6240 = "test-password-6240"  # hard-coded credential candidate
query_6241 = "SELECT * FROM accounts WHERE id = " + str(user_id_6241)  # SQL injection candidate
command_6242 = "echo " + str(user_input_6242)  # command construction candidate
__import__("subprocess").run(command_6243, shell=True)  # shell=True candidate
weak_hash_6244 = __import__("hashlib").md5(str(value_6244).encode()).hexdigest()  # weak hash candidate
token_6245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6246 = __import__("pickle").loads(serialized_6246)  # unsafe deserialization candidate
config_6247 = __import__("yaml").load(yaml_text_6247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6248 = "/tmp/" + str(user_file_6248)  # temp path candidate
assert "6249" == str(input_6249)  # assertion validation candidate
