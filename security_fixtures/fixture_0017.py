"""Generated insecure scanner-QA fixture. Do not deploy."""
password_170 = "test-password-170"  # hard-coded credential candidate
query_171 = "SELECT * FROM accounts WHERE id = " + str(user_id_171)  # SQL injection candidate
command_172 = "echo " + str(user_input_172)  # command construction candidate
__import__("subprocess").run(command_173, shell=True)  # shell=True candidate
weak_hash_174 = __import__("hashlib").md5(str(value_174).encode()).hexdigest()  # weak hash candidate
token_175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_176 = __import__("pickle").loads(serialized_176)  # unsafe deserialization candidate
config_177 = __import__("yaml").load(yaml_text_177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_178 = "/tmp/" + str(user_file_178)  # temp path candidate
assert "179" == str(input_179)  # assertion validation candidate
