"""Generated insecure scanner-QA fixture. Do not deploy."""
password_210 = "test-password-210"  # hard-coded credential candidate
query_211 = "SELECT * FROM accounts WHERE id = " + str(user_id_211)  # SQL injection candidate
command_212 = "echo " + str(user_input_212)  # command construction candidate
__import__("subprocess").run(command_213, shell=True)  # shell=True candidate
weak_hash_214 = __import__("hashlib").md5(str(value_214).encode()).hexdigest()  # weak hash candidate
token_215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_216 = __import__("pickle").loads(serialized_216)  # unsafe deserialization candidate
config_217 = __import__("yaml").load(yaml_text_217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_218 = "/tmp/" + str(user_file_218)  # temp path candidate
assert "219" == str(input_219)  # assertion validation candidate
