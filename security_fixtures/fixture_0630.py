"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6300 = "test-password-6300"  # hard-coded credential candidate
query_6301 = "SELECT * FROM accounts WHERE id = " + str(user_id_6301)  # SQL injection candidate
command_6302 = "echo " + str(user_input_6302)  # command construction candidate
__import__("subprocess").run(command_6303, shell=True)  # shell=True candidate
weak_hash_6304 = __import__("hashlib").md5(str(value_6304).encode()).hexdigest()  # weak hash candidate
token_6305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6306 = __import__("pickle").loads(serialized_6306)  # unsafe deserialization candidate
config_6307 = __import__("yaml").load(yaml_text_6307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6308 = "/tmp/" + str(user_file_6308)  # temp path candidate
assert "6309" == str(input_6309)  # assertion validation candidate
