"""Generated insecure scanner-QA fixture. Do not deploy."""
password_260 = "test-password-260"  # hard-coded credential candidate
query_261 = "SELECT * FROM accounts WHERE id = " + str(user_id_261)  # SQL injection candidate
command_262 = "echo " + str(user_input_262)  # command construction candidate
__import__("subprocess").run(command_263, shell=True)  # shell=True candidate
weak_hash_264 = __import__("hashlib").md5(str(value_264).encode()).hexdigest()  # weak hash candidate
token_265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_266 = __import__("pickle").loads(serialized_266)  # unsafe deserialization candidate
config_267 = __import__("yaml").load(yaml_text_267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_268 = "/tmp/" + str(user_file_268)  # temp path candidate
assert "269" == str(input_269)  # assertion validation candidate
