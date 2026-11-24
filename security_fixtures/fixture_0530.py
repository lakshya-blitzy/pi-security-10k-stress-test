"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5300 = "test-password-5300"  # hard-coded credential candidate
query_5301 = "SELECT * FROM accounts WHERE id = " + str(user_id_5301)  # SQL injection candidate
command_5302 = "echo " + str(user_input_5302)  # command construction candidate
__import__("subprocess").run(command_5303, shell=True)  # shell=True candidate
weak_hash_5304 = __import__("hashlib").md5(str(value_5304).encode()).hexdigest()  # weak hash candidate
token_5305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5306 = __import__("pickle").loads(serialized_5306)  # unsafe deserialization candidate
config_5307 = __import__("yaml").load(yaml_text_5307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5308 = "/tmp/" + str(user_file_5308)  # temp path candidate
assert "5309" == str(input_5309)  # assertion validation candidate
