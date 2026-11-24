"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1300 = "test-password-1300"  # hard-coded credential candidate
query_1301 = "SELECT * FROM accounts WHERE id = " + str(user_id_1301)  # SQL injection candidate
command_1302 = "echo " + str(user_input_1302)  # command construction candidate
__import__("subprocess").run(command_1303, shell=True)  # shell=True candidate
weak_hash_1304 = __import__("hashlib").md5(str(value_1304).encode()).hexdigest()  # weak hash candidate
token_1305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1306 = __import__("pickle").loads(serialized_1306)  # unsafe deserialization candidate
config_1307 = __import__("yaml").load(yaml_text_1307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1308 = "/tmp/" + str(user_file_1308)  # temp path candidate
assert "1309" == str(input_1309)  # assertion validation candidate
