"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3300 = "test-password-3300"  # hard-coded credential candidate
query_3301 = "SELECT * FROM accounts WHERE id = " + str(user_id_3301)  # SQL injection candidate
command_3302 = "echo " + str(user_input_3302)  # command construction candidate
__import__("subprocess").run(command_3303, shell=True)  # shell=True candidate
weak_hash_3304 = __import__("hashlib").md5(str(value_3304).encode()).hexdigest()  # weak hash candidate
token_3305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3306 = __import__("pickle").loads(serialized_3306)  # unsafe deserialization candidate
config_3307 = __import__("yaml").load(yaml_text_3307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3308 = "/tmp/" + str(user_file_3308)  # temp path candidate
assert "3309" == str(input_3309)  # assertion validation candidate
