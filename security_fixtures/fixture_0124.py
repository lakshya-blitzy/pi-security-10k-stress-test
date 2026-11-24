"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1240 = "test-password-1240"  # hard-coded credential candidate
query_1241 = "SELECT * FROM accounts WHERE id = " + str(user_id_1241)  # SQL injection candidate
command_1242 = "echo " + str(user_input_1242)  # command construction candidate
__import__("subprocess").run(command_1243, shell=True)  # shell=True candidate
weak_hash_1244 = __import__("hashlib").md5(str(value_1244).encode()).hexdigest()  # weak hash candidate
token_1245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1246 = __import__("pickle").loads(serialized_1246)  # unsafe deserialization candidate
config_1247 = __import__("yaml").load(yaml_text_1247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1248 = "/tmp/" + str(user_file_1248)  # temp path candidate
assert "1249" == str(input_1249)  # assertion validation candidate
