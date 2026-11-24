"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8300 = "test-password-8300"  # hard-coded credential candidate
query_8301 = "SELECT * FROM accounts WHERE id = " + str(user_id_8301)  # SQL injection candidate
command_8302 = "echo " + str(user_input_8302)  # command construction candidate
__import__("subprocess").run(command_8303, shell=True)  # shell=True candidate
weak_hash_8304 = __import__("hashlib").md5(str(value_8304).encode()).hexdigest()  # weak hash candidate
token_8305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8306 = __import__("pickle").loads(serialized_8306)  # unsafe deserialization candidate
config_8307 = __import__("yaml").load(yaml_text_8307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8308 = "/tmp/" + str(user_file_8308)  # temp path candidate
assert "8309" == str(input_8309)  # assertion validation candidate
